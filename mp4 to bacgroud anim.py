import os
from moviepy.editor import VideoFileClip

def convert_video_to_xvid(input_path, output_path):
    """
    Chuyển đổi video sang định dạng XviD với thông số kỹ thuật cụ thể:
    - Codec: Xvid (thông qua libxvid)
    - Resolution: 320x240 (4:3)
    - Frame rate: 15 FPS
    - Bitrate: ~2427 kb/s
    """
    try:
        # Kiểm tra file đầu vào
        if not os.path.exists(input_path):
            print(f"Lỗi: Không tìm thấy file {input_path}")
            return

        print(f"Đang xử lý: {input_path}...")
        
        # Load video
        clip = VideoFileClip(input_path)
        
        # Cấu hình các thông số theo yêu cầu
        # 1. Resize về 320x240
        # 2. Set frame rate về 15 fps
        target_clip = clip.resize(newsize=(320, 240)).set_fps(15)
        
        # Xuất file với codec libxvid
        # Lưu ý: ffmpeg cần có thư viện libxvid được cài đặt sẵn
        target_clip.write_videofile(
            output_path,
            codec="libxvid",
            bitrate="2427k",
            audio_codec="libmp3lame", # Xvid thường đi kèm với MP3
            temp_audiofile="temp-audio.m4a",
            remove_temp=True
        )
        
        print(f"Thành công! File đã được lưu tại: {output_path}")
        
    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình chuyển đổi: {e}")
    finally:
        # Giải phóng bộ nhớ
        if 'clip' in locals():
            clip.close()

if __name__ == "__main__":
    # Cấu hình đường dẫn file ở đây
    input_file = "uia.mp4" 
    output_file = "output_xvid.avi" # Xvid thường dùng container .avi
    
    convert_video_to_xvid(input_file, output_file)