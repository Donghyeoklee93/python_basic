import os
import csv
from post import Post

# file path
file_path = "./myvenv/chapter12/data.csv"

# list to save post object
post_list = []

# if data.csv exists
if os.path.exists(file_path):
    #loading post
    print("post is loading ")
    f = open(file_path, "r", encoding="utf8")
    reader = csv.reader(f)

    for data in reader:
        #generate Post instance
        post = Post(int(data[0]), data[1], data[2], int(data[3]))
        post_list.append(post)

else:
    #generate file
    f = open(file_path, "w", encoding="uft8", newline="")
    f.close()


# print(post_list[0].get_title())

#write post
def write_post():
    print("\n\n write post")
    title = input("Input the title\n>>>")
    content = input("Input the content\n>>>")

    #post number
    id = post_list[-1].get_id() + 1
    post = Post(id, title, content, 0)
    post_list.append(post)
    # print(post_list[id-1].get_title())
    print("posting is completed")

#list post
def list_post():
    # print(post_list)
    print("\n\n Post list")
    id_list = []
    for post in post_list:
        print("Number :", post.get_id())
        print("Title :", post.get_title())
        print("The number of viewing :", post.get_view_count())
        print("")
        id_list.append(post.get_id())
    
    while True:
        print("Q) Please enter the number of post (Enter -1 if you want to return to menu)")
        try:
            id = int(input(">>>"))
            if id in id_list:
                detail_post(id)
                break
            elif id == -1:
                break
            else:
                print("Not existed post number")
        except ValueError:
            print("Please enter the number")


# detail post
def detail_post(id):
    """ function to see post detail """
    print("\n\n Post detail")

    for post in post_list:
        if post.get_id()==id:
            post.add_view_count()
            print("Number :", post.get_id())
            print("Title :", post.get_title())
            print("Content :", post.get_content())
            print("The number of viewing :", post.get_view_count())
            target_post = post

    while True:
        print("Q) Modification: 1 Delete: 2 (Return to menu : -1)")
        try:
            choice = int(input(">>>"))
            if choice == 1:
                # print("modification")
                update_post(target_post)
                break
            elif choice == 2:
                # print("Delete")
                delete_post(target_post)
                break
            elif choice == -1:
                break
            else:
                print("Wrong input")
        except ValueError:
            print("Please enter the number")

# post modification
def update_post(target_post):
    """post modification"""
    print("\n\n Post modification")
    title = input("Please enter the title\n>>>")
    content = input("Please enter the content\n>>>")
    target_post.set_post(target_post.id, title, content, target_post.view_count)
    print("Post modification is completed")

# post delete
def delete_post(target_post):
    post_list.remove(target_post)


# save post
def save():
    f = open(file_path, "w", encoding="utf8", newline="")
    writer = csv.writer(f)

    for post in post_list:
        row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()]
        writer.writerow(row)
    f.close()
    print("Saving is completed")
    print("Exit program")

# print out menu

while True:
    print("\n\nMY BLOG")
    print("Please select menu")
    print("1. Write a post")
    print("2. List of posts")
    print("3. Exit the program")

    try:
        choice = int(input(">>>"))
    except ValueError:
        print("Please enter the number")
    else:
        if choice == 1:
            # print("Write a post")
            write_post()
        elif choice == 2:
            # print("List of posts")
            list_post()
        elif choice == 3:
            # print("Exit the program")
            save()
            break