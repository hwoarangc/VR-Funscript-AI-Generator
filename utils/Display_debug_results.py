from Debugger import Debugger

#video="/Users/k00gar/Downloads/BadoinkVR_Lights_Camera_Satisfaction_4K_HEVC_180_180x180_3dh.mp4"

#video = "/Users/k00gar/Downloads/Katrina Jade [ADD] Oct 16, 2024R_6kvr265_reenc.mp4"
video = "/Users/k00gar/Downloads/VideoFile.mp4"
#video = "/Users/k00gar/Downloads/ARPorn_Sasha Tatcha_Fit and Fired Up_4000p_8K_original_FISHEYE190_alpha.mp4"

#video = "/Users/k00gar/Downloads/2022-09-09 - TonightsGirlfriend - Kenna James.mp4"


# Katrina Jade ADD
frame = 77000
#frame = 126000

#BadoinkVR Lights Camera

#frame = 53100  # messed up bj

#frame = 90000
#frame = 77400

#Kenna James TNGF debug section
#frame = 80000
#frame = 36900
#frame = 153000 # says CG should be handjob
#frame = 75600
#frame = 100000 # should be grinding but BJ....
#frame = 72500  #BJ
#frame = 50400 #Grinding

#frame = 42920

#frame = 35312

debugger = Debugger(video, video[:-4])

debugger.load_logs()

#debugger.display_frame(frame)

debugger.play_video(frame, record=False, downsize_ratio=3)