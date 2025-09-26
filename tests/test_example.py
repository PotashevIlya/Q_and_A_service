from fastapi import status


# Примеры тестов.
class TestsEndpoints:

    def test_get_all_questions_endpoint(self, test_client, test_data):
        response = test_client.get("/questions/")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) > 0
        assert data[0]["text"] == "Тестовый вопрос"

    def test_get_answer_by_id_endpoint(self, test_client, test_data):
        response = test_client.get("/answers/1")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == 1
        assert data["text"] == "Тестовый ответ"
        assert data["question_id"] == 1
