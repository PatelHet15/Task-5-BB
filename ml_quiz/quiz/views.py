# quiz/views.py
from django.shortcuts import render, redirect
from .models import QuizQuestion

def home_view(request):
    return redirect('quiz_view')  

def quiz_view(request):
    score = 0
    total_questions = QuizQuestion.objects.count()
    
    if request.method == "POST":
        questions = QuizQuestion.objects.all()
        user_answers = []

        for question in questions:
            selected_answer = request.POST.get(f'answers_{question.question_no}')
            user_answers.append({
                'text': question.question,
                'user_answer': selected_answer,
                'right_answer': question.right_answer,
            })

            if selected_answer == question.right_answer:
                score += 1

        return render(request, 'results.html', {
            'score': score,
            'total_questions': total_questions,
            'questions': user_answers, 
        })

    questions = QuizQuestion.objects.all()

    processed_questions = [
        {
            'question_no': question.question_no,
            'text': question.question,
            'options': question.options, 
            'right_answer': question.right_answer
        }
        for question in questions
    ]

    return render(request, 'quiz.html', {'questions': processed_questions})


def results_view(request):
    selected_answers = request.session.get('selected_answers', []) 
    questions = QuizQuestion.objects.all()
    score = 0  

    for i, question in enumerate(questions):
        right_answer = question.right_answer  
        if i < len(selected_answers) and selected_answers[i] == right_answer:
            score += 1  

    return render(request, 'results.html', {'score': score}) 
