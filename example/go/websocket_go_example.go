
package main

import (
	"encoding/json"
	"github.com/gorilla/websocket"
	"log"
)

type Symbol struct {
	Code       string `json:"code"`
	DepthLevel int    `json:"depth_level"`
}

type Data struct {
	SymbolList []Symbol `json:"symbol_list"`
}

type Request struct {
	CmdID  int    `json:"cmd_id"`
	SeqID  int    `json:"seq_id"`
	Trace  string `json:"trace"`
	Data   Data   `json:"data"`
}

const(
	url = "wss://quote.aatest.online/quote-b-ws-api?token=3662a972-1a5d-4bb1-88b4-66ca0c402a03-1688712831841"
)

func websocket_example() {

	log.Println("Connecting to server at", url)

    c, _, err := websocket.DefaultDialer.Dial(url, nil)
    if err != nil {
        log.Fatal("dial:", err)
    }
    defer c.Close()

    //如果希望长时间运行，除了需要发送订阅之外，还需要修改代码，定时发送心跳，避免连接断开，具体查看接口文档
	req := Request{
		CmdID: 22002,
		SeqID: 123,
		Trace: "3baaa938-f92c-4a74-a228-fd49d5e2f8bc",
		Data:  Data{SymbolList: []Symbol{
			{"USDJPY",5},
			{"GOLD", 5},
		}},
	}
	messageBytes, err := json.Marshal(req)
	if err != nil {
		log.Println("json.Marshal error：", err)
		return
	}
	log.Println("req data：", string(messageBytes))

    err = c.WriteMessage(websocket.TextMessage, messageBytes)
    if err != nil {
        log.Println("write:", err)
    }

	rece_count := 0
	for{
		_, message, err := c.ReadMessage()

		if err != nil {
			log.Println("read:", err)
			break
		} else {
			log.Println("Received message:", string(message))
		}

		rece_count++
		if rece_count > 10 {
			break
		}
	}


}

