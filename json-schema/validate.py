import json, sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def json_validate(jsonobj):
    schemafile = 'schema.json'
    with open(schemafile, 'r') as f:
        myschema = json.loads(f.read())
    try:
        validate(myjson, myschema)
    except ValidationError, e:
        print 'json validate failed'
        print e


def password_match(jsonobj):
    passwordlist = [
        jsonobj.get("install_json", {}).get("nodeuser", {}).get("password"),
        jsonobj.get("install_json", {}).get("root_password"),
        jsonobj.get("update_json", {}).get("nodeuser", {}).get("password"),
        jsonobj.get("update_json", {}).get("root_password"),
        jsonobj.get("patch_json", {}).get("nodeuser", {}).get("password"),
        jsonobj.get("patch_json", {}).get("root_password"),
        jsonobj.get("verify_json", {}).get("nodeuser", {}).get("password"),
        jsonobj.get("verify_json", {}).get("root_password")
    ]
    count = 0
    password = ""
    for i in passwordlist:
        if not i:
            continue
        if i and not count:
            password = i
            count = count + 1
            continue
        if i and i != password:
            print 'password match failed'
            sys.exit(1)


if __name__ == "__main__":
    myjsonfile = sys.argv[1]
    with open(myjsonfile, 'r') as f:
        myjson = json.loads(f.read())
    json_validate(myjson)
    password_match(myjson)
    print 'pod config validate succeeded'
