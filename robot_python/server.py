# Flask 모듈을 임포트합니다. Flask 클래스는 웹 애플리케이션을 만드는 데 사용됩니다.
from flask import Flask, render_template, request, redirect, url_for

# Flask 인스턴스를 생성합니다. 이 인스턴스를 통해 애플리케이션이 실행됩니다.
app = Flask(__name__)

# 글로벌 카운터 변수를 선언합니다. 이 변수는 방문자가 버튼을 누를 때마다 증가됩니다.
counter = 0

# 루트 URL('/')에 대한 라우트를 정의합니다. 
# 이 함수는 웹사이트에 접속했을 때 표시되는 메인 페이지를 결정합니다.
@app.route('/')
def index():
    # 글로벌 변수를 사용하기 위해 global 키워드를 사용합니다.
    global counter
    # 'index.html' 템플릿을 렌더링하고, 그 과정에서 counter 변수의 값을 템플릿에 전달합니다.
    return render_template('index.html', counter=counter)

# '/increment' URL에 대한 라우트를 정의하고, POST 요청을 처리하는 함수를 정의합니다.
@app.route('/increment', methods=['POST'])
def increment():
    # 글로벌 변수를 사용하기 위해 global 키워드를 사용합니다.
    global counter
    # 카운터를 1 증가시킵니다.
    counter += 1
    # 사용자를 홈 페이지('/')로 리다이렉트합니다.
    return redirect(url_for('index'))

# 이 스크립트가 직접 실행되었을 때만 아래의 코드가 실행됩니다.
# 즉, 이 스크립트가 다른 스크립트에 의해 임포트되어 사용되는 것이 아니라,
# 직접 실행되었을 때 웹 서버가 시작됩니다.
if __name__ == '__main__':
    # 앱을 실행하고, debug=True로 설정하여 개발 중에 디버그 정보를 활성화합니다.
    app.run(debug=True)
