# Отчёт

- ФИО: [Анчугов Михаил Олегович]
- Вариант стенда: s07
- Репозиторий: [https://github.com/Viva1019/test]

| № | PR | Итог |
|---|---|---|
| 01 | [https://github.com/Viva1019/test/pull/1] | [Выполнены три reset (soft, mixed, hard). В протоколе зафиксированы теги до сброса и различия в статусе индекса/рабочего файла. В истории PR видны три force-push.] |
| 02 | [https://github.com/Viva1019/test/pull/2] | [Успешный rebase ветки `feature/task-02` на `base/task-02`. Конфликт разрешён, merge-коммита нет, коммиты получили новые SHA. В `evidence` добавлен вывод `git range-diff`.] |
| 03 | [https://github.com/Viva1019/test/pull/3] | [Два события force-push. История сокращена до 3 коммитов (reword, squash, pick). В протоколе доказано совпадение хешей деревьев до и после операций.] |
| 04 | [https://github.com/Viva1019/test/pull/4] | [Коммит R полностью отменяет X. Коммит Z через `git restore` возвращает только `settings.ini` в состояние до Y, при этом правки в `message.txt` из коммита Y сохранены.] |
| 05 | [https://github.com/Viva1019/test/pull/5] | [Создан merge-коммит M. Проверка через `git cat-file` подтверждает наличие двух родителей (локальный L и удалённый R). Оба файла присутствуют в репозитории.] |
| 06 | [https://github.com/Viva1019/test/pull/6] | [История осталась линейной (без merge-коммита). Локальный коммит L был перебазирован поверх R и получил новый SHA (L').] |
| 07 | [https://github.com/Viva1019/test/pull/7] | [Опубликованы два тега. `git cat-file -t` подтверждает: `v1.0.0` имеет тип `tag` (annotated), а `v1.1.0-rc1` имеет тип `commit` (lightweight).] |
| 08 | [https://github.com/Viva1019/test/pull/8] | [Состояния staged, unstaged и untracked успешно сохранены через `stash -u` и восстановлены через `apply --index` после коммита хотфикса.] |
| 09 | [https://github.com/Viva1019/test/pull/9] | [Коммит LOST восстановлен через `git reflog` после `reset --hard`. SHA восстановленного коммита на GitHub в точности совпадает с исходным.] |
| 10 | [https://github.com/Viva1019/test/pull/10] | [Выполнен `cherry-pick -x` только для коммита D2. В сообщении нового коммита есть ссылка на оригинал, файлы из D1 и D3 в ветку не попали.] |
| 11 | [https://github.com/Viva1019/test/pull/11] | [`git blame` указал на проблемную строку. Ручной и автоматический `bisect` нашли один и тот же bad-коммит (`f9723d13`). Ошибка исправлена, `python3 check.py` выводит `OK`.] |
| 12 | [https://github.com/Viva1019/test/pull/12] | [Настроены правила `.gitignore` (включая инверсию для `.gitkeep`). Файл `debug.log` удалён из индекса через `git rm --cached`, но физически остался на диске.] |
