echo 'Medidas tomadas ᕕ( ᐛ )ᕗ'
echo '\nIgnora el siguiente output de terminal :)\n- - -'
mysqldump -B --add-drop-database -u root -p"mac_15_db" reto_iot > db.sql # the secret is out pt2 T-T
git add db.sql
git commit -m "Update DB"
git push
echo '- - -\n'