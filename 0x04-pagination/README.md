# 0x04. Pagination

## Description

What you should learn from this project:

* How to paginate a dataset with simple page and page_size parameters
* How to paginate a dataset with hypermedia metadata
* How to paginate in a deletion-resilient manner

---

### [0. Simple helper function](./0-simple_helper_function.py)

* Write a function named index_range that takes two integer arguments page and page_size.

### [1. Simple pagination](./1-simple_pagination.py)

* Copy index_range from the previous task and the following class into your code

### [2. Hypermedia pagination](./2-hypermedia_pagination.py)

* Replicate code from the previous task.

### [3. Deletion-resilient hypermedia pagination](./3-hypermedia_del_pagination.py)

* The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

---

## Author

**Joshua Martinez** - [dantsub](https://github.com/dantsub) :octocat:
