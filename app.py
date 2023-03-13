import logging



#region 主程式碼


try:

    #region Logging 設定

    logging.basicConfig(level=logging.WARNING, filename='./log.txt',
        format='[%(asctime)s %(levelname)-8s] %(message)s',
        datefmt='%Y%m%d %H:%M:%S',
        )

    #endregion




except Exception as e:
    logging.critical("主程式發生錯誤! ", exc_info=True)



#endregion