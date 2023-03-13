import logging
import configparser
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler

#region 主程式碼


try:

    #region Logging 設定

    logging.basicConfig(level=logging.WARNING, filename='./log.txt',
        format='[%(asctime)s %(levelname)-8s] %(message)s',
        datefmt='%Y%m%d %H:%M:%S',
        )

    #endregion

    #region 讀取config設定檔

    config = configparser.ConfigParser()
    config.read('config.ini', encoding="utf-8")

    #endregion

    #建立實體
    app = Flask(__name__)

    #LINE Bot 設定
    line_bot_api = LineBotApi(config.get('protobot1', 'channel_access_token'))
    handler = WebhookHandler(config.get('protobot1', 'channel_secret'))


except Exception as e:
    logging.critical("主程式發生錯誤! ", exc_info=True)



#endregion

#啟動程式
if __name__ == "__main__":
    app.run()