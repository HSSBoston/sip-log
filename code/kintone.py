import adafruit_requests
import json, wifi, os, adafruit_connection_manager

wifi.radio.connect(ssid=os.getenv("CIRCUITPY_WIFI_SSID"),
                   password=os.getenv("CIRCUITPY_WIFI_PASSWORD"))
print("IP address:", wifi.radio.ipv4_address)

pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)
requests = adafruit_requests.Session(pool, ssl_context)

# Uploads a new record to a Kintone app
#   subDomain (string): Name of a subdomain where the Kitone app runs
#   apiToken (string):  API token to access the Kintone app
#   record (dict):      Dictionary form of JSON record to be uploaded
#
#   Returns the uploaded record's ID in string or raises a RuntimeError if the upload failed.
#
#   This function accepts keyword arguments only. 
#
def uploadRecord(subDomain, apiToken, record):
    url = "https://" + subDomain + ".kintone.com/k/v1/record.json"
    headers = {"X-Cybozu-API-Token": apiToken,
               "Content-Type": "application/json"}
    
    response = requests.post(url, headers=headers, json=record)
    
    if response.status_code == 200 and "id" in json.loads(response.text):
        print("Record uploaded.", end=" ")
        recordId = json.loads(response.text)["id"]
        print("Record ID: " + recordId)
        return recordId
    else:
        raise RuntimeError("Record upload failed. Status code: " + str(response.status_code))

def uploadSipLog(subDomain, appId, apiToken, pitch):
    payload = {"app": appId,
               "record": {"pitch": {"value": pitch }}}
    recordId = uploadRecord(subDomain=subDomain,
                            apiToken=apiToken,
                            record=payload)
    
def uploadAlert(subDomain, appId, apiToken, alert):
    payload = {"app": appId,
               "record": {"alert": {"value": alert }}}
    recordId = uploadRecord(subDomain=subDomain,
                            apiToken=apiToken,
                            record=payload)
