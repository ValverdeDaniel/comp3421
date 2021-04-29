select * from henry_book;


select DISTINCT TYPE from henry_book;

select book.TITLE, book.TYPE from henry_book as book where book.TYPE = 'SFI';

select * from henry_book as book
WHERE book.TYPE IS NOT NULL;

SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE, book.TITLE
FROM henry_book as book
JOIN henry_inventory as inventory
ON book.BOOK_CODE = inventory.BOOK_CODE
JOIN henry_branch as branch
ON inventory.BRANCH_NUM = branch.BRANCH_NUM
WHERE book.TYPE = 'SFI' AND book.TITLE = 'Harry Potter and the Goblet of Fire';