import numpy as np

A = np.array([ [1,2], [3,4] ])
B = np.array([ [0,1], [1,0] ])
C = A@B
print(f"行列CはAとBの行列積であり，結果は\n{C}\nです。")