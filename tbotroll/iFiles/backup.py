def getUrl(gmessage):
    global irul
    mid = gmessage.chat.id
    tid = '/'.join(gmessage.text.split('/')[5:][:-1])
    print(tid)
    includeData = f"https://sheets.googleapis.com/v4/spreadsheets/1Nc3gkg-sGfrj84ludywF-eixv4oNoul38lsYq456t-Y?includeGridData=True&access_token={access_token}"
    surl1 = f"https://sheets.googleapis.com/v4/spreadsheets/{tid}/values/{isheet.sid1}"
    surl2 = f"https://sheets.googleapis.com/v4/spreadsheets/{tid}/values/{isheet.sid2}"
    try:
        tg.send_message(mid, "������� ��������...")
        gtest_col1 = requests.get(f"{surl1}!A:A?access_token={access_token}&majorDimension=COLUMNS")
        print(gtest_col1)
        if gtest_col1.status_code != 200:
            tg.send_message(mid, f"{isheet.sid1} � ���� �������� - ?")
        else:
            tg.send_message(mid, f"{isheet.sid1} � ���� �������� - ??")
        gtest_rows1 = requests.get(f"{surl1}!A:O?access_token={access_token}&majorDimension=ROWS")
        tg.send_message(mid, "33%")
        if gtest_rows1.status_code != 200:
            tg.send_message(mid, f"{isheet.sid1} � ���� ����� - ?")
        else:
            tg.send_message(mid, f"{isheet.sid1} � ���� ����� - ??")
        gtest_urls1 = requests.get(f"{surl1}!C:C?access_token={access_token}&majorDimension=COLUMNS")
        tg.send_message(mid, "40%")
        if gtest_urls1.status_code != 200:
            tg.send_message(mid, f"{isheet.sid1} ������ - ?")
        else:
            tg.send_message(mid, f"{isheet.sid1} ������ - ??")
        gtest_col2 = requests.get(f"{surl1}!A:O?access_token={access_token}&majorDimension=COLUMNS")
        tg.send_message(mid, "56%")
        if gtest_col2.status_code != 200:
            tg.send_message(mid, f"{isheet.sid2} � ���� �������� - ?")
        else:
            tg.send_message(mid, f"{isheet.sid2} � ���� �������� - ??")
        gtest_rows2 = requests.get(f"{surl2}!A:O?access_token={access_token}&majorDimension=ROWS")
        tg.send_message(mid, "82%")
        if gtest_rows2.status_code != 200:
            tg.send_message(mid, f"{isheet.sid2} � ���� ����� - ?")
        else:
            tg.send_message(mid, f"{isheet.sid2} � ���� ����� - ??")
        gtest_urls2 = requests.get(f"{surl2}!C:C?access_token={access_token}&majorDimension=COLUMNS")
        if gtest_urls2.status_code != 200:
            tg.send_message(mid, f"{isheet.sid2} ������ - ?")
        else:
            tg.send_message(mid, f"{isheet.sid2} ������ - ??")
        tg.send_message(mid, "100%")
        if gtest_col1.status_code == 200:
            tg.send_message(mid, "��������:)")
            '''������� ������� ����� ��������� ���� � � ���� ��� ��� ��� ���������'''
            print('�� ��� ��� ������� ����� ��...')
            addFile(gtest_col1, gtest_rows1, gtest_urls1, gtest_col2, gtest_rows2, gtest_urls2, True, mid)
            return sendFirstMessage(gmessage)
        else:
            checkpoint = tg.send_message((mid, f"������ {gtest_col1.status_code}, �������� ����� ��� ���"))
    except:
        if gtest_col1.status_code == 403:
            checkpoint = tg.send_message(mid, f"������ {gtest_col1.status_code}, �������� �������� �� �����, "
                                         f"�������� ��� ���")
            return sendFirstMessage(gmessage)
        if gtest_col1.status_code == 404:
            tg.send_message(mid, f"����� ������� �� ���������� ({gtest_col1.status_code}), �������� ����� ��� ���")
            return sendFirstMessage(gmessage)
        if gtest_col1.status_code == 400:
            tg.send_message(mid,
                            f"� ������ �� ��������, � ���� {gtest_col1.status_code}, ���������� ��������"
                            f"������!")
            return sendFirstMessage(gmessage)
