import os
os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['CONDA_PREFIX'] + r"\Library\bin\graphviz"

import pydotplus
from PIL import Image
import matplotlib.pyplot as plt

def show(tree):
      """Creates a DOT file of the tree and displays the tree
      
      Parameters
      ----------
      tree : PST
             Probabilistic suffix tree object
      """
      
      f = open("PST.dot", 'w')
      f.write("graph PST {\n")
      f.write("node0" + "[label = Root];\n")
      temp = [tree.root]
      index = [0]
      j = 1
      while len(temp):
          parent = temp.pop(0)
          i = index.pop(0)
          current = parent.getChild()
          while(current != None):
              f.write("node" + str(j) + "[label = " + str(current.getData()) + "];\n")
              f.write("\"node" + str(i) + "\" -- " + "\"node" + str(j) +
                      "\"[label = " + str(current.getCount()) + "]" + ";\n")
              temp.append(current)
              current = current.getNext()
              index.append(j)
              j += 1
      f.write("}")
      f.close()
      graph = pydotplus.graph_from_dot_file("PST.dot")
      graph.write_png("PST.png")
      img = Image.open("PST.png")
      plt.imshow(img)
      plt.axis("off")
