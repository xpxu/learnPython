# -*- coding:utf-8 -*-

import threading
import weakref

def _make_id(target):
    if hasattr(target, '__func__'):
        return (id(target.__self__), id(target.__func__))
    return id(target)

# 全局变量
NONE_ID = _make_id(None)
NO_RECEIVERS = object()



class Signal(object):
    def __init__(self, providing_args=None, use_caching=False):
        '''
        ------------------------------------
        sender_receivers_cache is a weakref.WeakKeyDictionary like:
        {
         weakref.ref(sender1):　[weakref.ref(receiver),],
         weakref.ref(sende2):　NON_RECEIVER，
         ...
         }
         当sender对象的强引用消亡时，字典中的这条记录将自动消失。
         当receiver对象的强引用消亡时，weakref.ref(receiver)会变成None
        ------------------------------------
        receivers is like:
        [((receiver_id, sender_id), weakref.ref(receiver)), ... ]
        当receiver对象的强引用消亡时，weakref.ref(receiver)()会自动变成None.
        ------------------------------------
        '''
        self.receivers = []
        if providing_args is None:
            providing_args = []
        self.lock = threading.Lock()
        self.use_caching = use_caching
        self.sender_receivers_cache = weakref.WeakKeyDictionary() if use_caching else {}
        self._dead_receivers = False

    def connect(self, receiver, sender=None, weak=True, dispatch_uid=None):
        '''
        receiver有两种可能：
        1. 普通method
        2. instance method
        '''

        if dispatch_uid:
            lookup_key = (dispatch_id, _make_id(sender))
        else:
            lookup_key = (_make_id(receiver), _make_id(sender))
        if weak:
            ref = weakref.ref
            receiver = ref(receiver, self._remove_receiver)
        with self.lock:
            # 清除被回收的receiver对象在列表中的记录
            self._clear_dead_receivers()
            for r_key, _ in self.receivers:
                if r_key == lookup_key:
                    break
            else:
                self.receivers.append(((lookup_key), receiver))

            # 清空缓存
            self.sender_receivers_cache.clear()

    def _clear_dead_receivers(self):
        # Note: caller is assumed to hold self.lock.
        if self._dead_receivers:
            self._dead_receivers = False
            new_receivers = []
            for r in self.receivers:
                if isinstance(r[1], weakref.ReferenceType) and r[1]() is None:
                    continue
                new_receivers.append(r)
            self.receivers = new_receivers

    def _remove_receiver(self, receiver=None):
        self._dead_receivers = True

    def _live_receivers(self, sender):
        receivers = None
        if self.use_caching and not self._dead_receivers:
            receivers = self.sender_receivers_cache.get(sender)
            if receivers is NO_RECEIVERS:
                return []
        if receivers is None:
            with self.lock:
                self._clear_dead_receivers()
                senderkey = _make_id(sender)
                receivers = []
                for (receiverkey, r_senderkey), receiver in self.receivers:
                    if r_senderkey == NONE_ID or r_senderkey == senderkey:
                        receivers.append(receiver)
                if self.use_caching:
                    if not receivers:
                        self.sender_receivers_cache[sender] = NO_RECEIVERS
                    else:
                        # Note, we must cache the weakref versions
                        self.sender_receivers_cache[sender] = receivers
        # 这里non_weak的意思是，把weakref version对象dereference.
        non_weak_receivers = []
        for receiver in receivers:
            if isinstance(receiver, weakref.ReferenceType):
                # Dereference the weak reference.
                receiver = receiver()
                if receiver is not None:
                    non_weak_receivers.append(receiver)
            else:
                non_weak_receivers.append(receiver)
        return non_weak_receivers

    def send(self, sender, **named):
        responses = []
        if not self.receivers or self.sender_receivers_cache.get(sender) is NO_RECEIVERS:
            return responses

        for receiver in self._live_receivers(sender):
            response = receiver(signal=self, sender=sender, **named)
            responses.append((receiver, response))
        return responses