import json
def saved_data_helper(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)
def load_data():
    try:
        with open("youtube.txt","r") as file:
          test =json.load(file)
          return test;
    except FileNotFoundError:
        return[]

def list_all_videos(videos):
    for index,video in enumerate(videos,start=1):
        print(f"{index} .{video["name"]},Duration is : {video["time"]}")

def add_video(videos):
    name = input("Enter video name :")
    time = input("enter vido time :");
    videos.append({"name": name, "time":time});
    saved_data_helper(videos);

def uptade_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to uptade"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video : ");
        time = input("Enter the new video time : ")
        videos[index-1]={"name":name,"time":time}
        saved_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index which to be deleted : "));
    if 1 <= index <= len(videos):
        del videos[index - 1]
        saved_data_helper(videos)
    else:
        print("Invalid video index selected ") 

def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 
