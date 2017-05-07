import java.lang.Thread;
//import java.util.*;


class MyThread extends Thread {
    int x = 0;
    public void run(){
        while(true){
            x = x ^ 1;
        } 
    }
}


public class deadloop {
    public static void main(String[] args) throws Exception{
        for (int i = 0; i < Runtime.getRuntime().availableProcessors(); i++){
            Thread myThread = new MyThread();
            System.out.println("start thread" + i);
            myThread.start();            
        }
    }



}

