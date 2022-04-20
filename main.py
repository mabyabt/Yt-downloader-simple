# importing the module
from pytube import YouTube

def on_complete(stream,file_path):
    print(file_path)
    print(stream)

def on_progress(stream,chunk,bytes_remaining):
    print(100- (bytes_remaining/stream.filesize*100))


link = input('YouTube link:')


video_object = YouTube(link,
                       on_complete_callback= on_complete,
                       on_progress_callback= on_progress)




# vid info
print(f'title: {video_object.title}')
print(f'{video_object.length/60} mins')
print(f'author: {video_object.author}')
print(video_object.description)




#vid download
print('download (b)est | (w)orst | (a)udio | (e)xit' )
download_choice = input('choice: ')
match download_choice:
    case 'b':
        video_object.streams.get_highest_resolution().download()
    case 'w':
        video_object.streams.get_lowest_resolution().download()
    case 'a' :
        video_object.streams.get_audio_only().download()
    case 'e':
        exit()
