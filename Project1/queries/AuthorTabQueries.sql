#Author Queries
SELECT AUTHOR_NUM, AUTHOR_LAST FROM henry_author Where AUTHOR_LAST = 'Morrison';

select book.TITLE
from henry_author as author
join henry_wrote as wrote
ON author.AUTHOR_NUM = wrote.AUTHOR_NUM
JOIN henry_book as book
on wrote.BOOK_CODE = book.BOOK_CODE
WHERE author.AUTHOR_LAST = 'Morrison';

SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE
FROM henry_book as book
JOIN henry_inventory as inventory
ON book.BOOK_CODE = inventory.BOOK_CODE
JOIN henry_branch as branch
ON inventory.BRANCH_NUM = branch.BRANCH_NUM
WHERE book.TITLE = 'A Guide To SQL';

