#Tensor Import
import tensorflow as tf

#Init two constants
x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

#multiply
result = tf.multiply(x1, x2)
sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
print(sess.run(result))
#close the current session
sess.close()
