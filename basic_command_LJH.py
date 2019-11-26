import pickle
import sys
ID = None
PASSWORD = None


def load_info():  # 파일에서 아이디랑 비밀번호 정보를 불러옴
    global ID, PASSWORD
    try:
        idf = open('idf', 'rb')
        pwf = open('pwf', 'wb')
        ID = pickle.load(idf)
        PASSWORD = pickle.load(pwf)
        idf.close()
        pwf.close()

    except:
        pass


def dump_info(string, file):  # 파일에 정보 업로드
    a_file = open(file, 'wb')
    pickle.dump(string, a_file)
    a_file.close()


def print_help():  # 설명서 출력
    print(
          'setting - ID와 PASSWORD 를 설정합니다. \n'
          "gmail   - 로그인 방식을 'gmail을 통한 로그인' 으로 설정합니다.\n"
          "sign_in - 로그인 방식을 '일반적인 로그인 방식' 으로 설정합니다.\n"
          'check   - 설정한 ID와 PASSWORD를 확인합니다. \n'
          'reset   - ID와 PASSWORD 를 초기화합니다.\n'
          'exit    - 프로그램을 종료합니다.'
          )


def setting():  # 아이디와 비밀번호를 변경하여 내장파일에 저장하는 함수
    set_id = input("설정하고자 하는 ID를 입력해주세요 : ")
    set_pw = input("설정하고자 하는 PASSWORD를 입력해주세요 : ")
    dump_info(set_id, 'idf')
    dump_info(set_pw, 'pwf')


def gmail():  # 로그인 방식을 gmail로 바꾸는 함수
    btn = 'btn.flat'
    print("로그인 방식이 gmail로 설정되었습니다.")


def sign_in():  # 로그인 방식을 sign_으로 바꾸는 함수
    btn = 'btn.info'
    print("로그인 방식이 기본방식으로 설정되었습니다.")


def check():  # 아이디와 비밀번호 확인 함수
    if ID is None:
        print("ID와 PASSWORD가 설정되지 않았습니다.")
    else:
        print("ID :", ID, "\nPASSWORD :", PASSWORD)


def reset():  # 프로그램 내 저장되어있는 아이디와 비밀번호를 초기화하는 함수
    dump_info(None, 'idf')
    dump_info(None, 'pwf')
    print("ID와 PASSWORD의 초기화가 완료되었습니다.")


def exit():  # 프로그램을 종료시키는 함수
    print("프로그램을 종료합니다.")
    sys.exit(0)


commandlist = {'help': print_help, 'setting': setting, 'check': check,
               'gmail': gmail, 'sign_in': sign_in, 'reset': reset, 'exit': exit}

# 함수 이름과 함수를 연결한 딕셔너리. 이를 통해 명령어로 함수를 실행시킬 수 있도록 함


###
# 여기는 비어있는공간
# 테스트용 main함수와 분리하기 위함
###


if __name__ == '__main__':
    while True:
        command = input('>')
        print(command)
        try:
            func = commandlist[command]
            func()
        except KeyError:
            print("해당하는 명령어가 없습니다.")
