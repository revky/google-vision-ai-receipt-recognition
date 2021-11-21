from file_manager import main


test_limit = range(5,15)
cred = 'receipt-recognition-330315-3824ec090746.json'
path = 'C:\\Users\\filip\\Desktop\\google-vision-ai-receipt-recognition\\recipts\\249236944_570647567363571_7413693291870444864_n.jpg'

for limit in test_limit:
    main(cred, path, limit)