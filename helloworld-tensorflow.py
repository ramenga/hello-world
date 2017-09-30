'''
****************************************
  Tensorflow Hello World
****************************************
'''

import tensorflow as tf

x = tf.placeholder(tf.string,name='x')
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)
  print(sess.run(x,feed_dict = {x:"Hello World"}))

sess.close()
