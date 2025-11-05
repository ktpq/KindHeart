docker compose up -d --build
docker exec -it kindheart-backend sh -c "python manage.py migrate"
Get-Content init.sql | docker-compose exec -T db psql -U postgres -d KindHeart

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', '1234')" | docker exec -i kindheart-backend python manage.py shell