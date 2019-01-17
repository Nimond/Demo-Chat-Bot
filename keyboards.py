import json

default_keyboard = str(json.dumps({ 
    "one_time": False, 
    "buttons": [ 
      [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"key1\"}", 
          "label": "Red" 
        }, 
        "color": "negative" 
      }, 
     { 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"key2\"}", 
          "label": "Green" 
        }, 
        "color": "positive" 
      }], 
      [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"key3\"}", 
          "label": "White" 
        }, 
        "color": "default" 
      }, 
     { 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"key4\"}", 
          "label": "Blue" 
        }, 
        "color": "primary" 
      }] 
    ] 
  } ))
 