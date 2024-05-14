import random
import openai

openai.api_key = ''  # 여기에 실제 API 키를 넣어야 합니다.

def get_random_question(field):
    questions = {
        "CS": ["데이터 구조란 무엇인가요?", "알고리즘 효율성을 평가하는 기준은 무엇인가요?", "가비지 컬렉션의 원리는 무엇인가요?"],
        "FE": ["리액트와 앵귤러의 차이점은 무엇인가요?", "프론트엔드 최적화 기법에는 어떤 것들이 있나요?", "웹 접근성이란 무엇인가요?"],
        "BE": ["REST API란 무엇인가요?", "마이크로서비스 아키텍처의 장단점은 무엇인가요?", "OAuth 인증 방식에 대해 설명해주세요."],
        "DB": ["SQL과 NoSQL의 차이점은 무엇인가요?", "트랜잭션 격리 수준에 대해 설명해주세요.", "데이터베이스 샤딩의 원리는 무엇인가요?"],
        "OOP": ["상속과 구성의 차이점은 무엇인가요?", "다형성을 설명해주세요.", "캡슐화가 중요한 이유는 무엇인가요?"]
    }
    return random.choice(questions[field])

def initialize_interview():
    print("안녕하세요. 면접에 참여해주셔서 감사합니다.")

def run_interview_session(fields, questions_per_field):
    for field in fields:
        print(f"\n{field} 분야 면접을 시작하겠습니다.")
        main_question = get_random_question(field)
        print(f"면접관 : {main_question}")
        user_response = input("면접자 : ")
        follow_up_count = 0

        messages = [
            {"role": "system", "content": "This is an interview simulation."},
            {"role": "user", "content": user_response}
        ]

        while follow_up_count < questions_per_field[field]:
            response = openai.ChatCompletion.create(
                model="",
                messages=messages,
                temperature=0.5,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            follow_up_question = response['choices'][0]['message']['content']
            print(f"면접관 : {follow_up_question}")
            main_question = follow_up_question  # Update main question for continuity
            user_response = input("면접자 : ")
            messages.append({"role": "assistant", "content": follow_up_question})
            messages.append({"role": "user", "content": user_response})
            follow_up_count += 1
        
        print(f"{field} 분야 면접을 종료합니다.")

    print("모든 면접이 종료되었습니다. 수고하셨습니다.")

# Example usage
fields = ["CS", "FE", "BE", "DB", "OOP"]
questions_per_field = {"CS": 2, "FE": 3, "BE": 2, "DB": 2, "OOP": 2}
initialize_interview()
run_interview_session(fields, questions_per_field)