import json

default_keyboard = str(json.dumps({ 
    "one_time": False, 
    "buttons": [ 
      [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"red\"}", 
          "label": "Red" 
        }, 
        "color": "negative" 
      }, 
     { 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"green\"}", 
          "label": "Green" 
        }, 
        "color": "positive" 
      }], 
      [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"white\"}", 
          "label": "White" 
        }, 
        "color": "default" 
      }, 
     { 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"blue\"}", 
          "label": "Blue" 
        }, 
        "color": "primary" 
      }] 
    ,
    [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"close\"}", 
          "label": "Close" 
        }, 
        "color": "negative" 
      }]
      ]
  }))

closed_keyboard = str(json.dumps({ 
    "one_time": True, 
    "buttons": [ 
      [{ 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"open\"}", 
          "label": "Open" 
        }, 
        "color": "positive" 
      }], 
      [ 
      { 
        "action": { 
          "type": "text", 
          "payload": "{\"button\": \"close_full\"}", 
          "label": "Close" 
        }, 
        "color": "negative" 
      }] 
    ] 
  } ))

empty = str(json.dumps({}))
 