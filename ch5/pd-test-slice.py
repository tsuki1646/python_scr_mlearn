import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')
import pandas as pd
# 身長・体重・タイプのデータフレームを生成
tbl = pd.DataFrame({
    "weight": [ 80.0, 70.4, 65.5, 45.9, 51.2, 72.5 ],
    "height": [ 170,  180,  155,  143,  154,  160  ],
    "type":   [ "f",  "n",  "n",  "t",  "t",  "f"  ]
})

# (0から数えて)2から3つ目のデータを表示
print("tbl[2:4]\n", tbl[2:4])

# (0から数えて)3つ目以降のデータを表示
print("tbl[2:]\n",tbl[3:])
