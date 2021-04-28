select * from henry_publisher;

select PUBLISHER_NAME from henry_publisher;

SELECT * 
FROM henry_publisher as publisher
JOIN henry_book as book
ON publisher.PUBLISHER_CODE = book.PUBLISHER_CODE
WHERE PUBLISHER_NAME = "Basic Books";

##NEED to update other branch query in python to utilize this
SELECT branch.BRANCH_NAME, inventory.ON_HAND, book.PRICE
FROM henry_book as book
JOIN henry_inventory as inventory
ON book.BOOK_CODE = inventory.BOOK_CODE
JOIN henry_branch as branch
ON inventory.BRANCH_NUM = branch.BRANCH_NUM
JOIN henry_publisher as publisher
ON publisher.PUBLISHER_CODE = book.PUBLISHER_CODE
WHERE book.TITLE = 'Godel, Escher, Bach' AND publisher.PUBLISHER_NAME = "Basic Books";