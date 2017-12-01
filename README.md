# fieldeng-pyscythe

## Interpolation

For input df:

function,time,value
sig1Raw, 2017-04-01 12:00, 0.0
sig1Raw, 2017-04-01 12:01, 0.5
sig1Raw, 2017-04-01 12:02, 1.0
sig1Raw, 2017-04-01 12:03, 0.5
sig1Raw, 2017-04-01 12:04, 1.0
sig1Raw, 2017-04-01 12:05, 0.0
sig1Raw, 2017-04-01 12:06, 0.5
sig1Raw, 2017-04-01 12:07, 1.0
sig1Raw, 2017-04-01 12:09, 1.0
sig1Raw, 2017-04-01 12:10, 1.0
sig1Raw, 2017-04-01 12:11, 1.0
sig1Raw, 2017-04-01 12:12, 5.0
sig2Raw, 2017-04-01 12:00, 2.0
sig2Raw, 2017-04-01 12:05, 4.0
sig2Raw, 2017-04-01 12:06, 3.0
sig2Raw, 2017-04-01 12:12, 2.0

list = ['sig1Raw','sig2Raw']

interpolate('sig1Raw', list, 'function', df)

{'sig1Raw': [[['sig1Raw', Timestamp('2017-04-01 12:00:00'), 0.0]], [['sig1Raw', Timestamp('2017-04-01 12:01:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:02:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:03:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:04:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:05:00'), 0.0]], [['sig1Raw', Timestamp('2017-04-01 12:06:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:07:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:08:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:09:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:10:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:11:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:12:00'), 5.0]]], 'sig2Raw': [[['sig2Raw', Timestamp('2017-04-01 12:00:00'), 2.0]], [['sig2Raw', Timestamp('2017-04-01 12:01:00'), 2.4]], [['sig2Raw', Timestamp('2017-04-01 12:02:00'), 2.8]], [['sig2Raw', Timestamp('2017-04-01 12:03:00'), 3.2]], [['sig2Raw', Timestamp('2017-04-01 12:04:00'), 3.6]], [['sig2Raw', Timestamp('2017-04-01 12:05:00'), 4.0]], [['sig2Raw', Timestamp('2017-04-01 12:06:00'), 3.0]], [['sig2Raw', Timestamp('2017-04-01 12:07:00'), 2.8333333333333335]], [['sig2Raw', Timestamp('2017-04-01 12:08:00'), 2.6666666666666665]], [['sig2Raw', Timestamp('2017-04-01 12:09:00'), 2.5]], [['sig2Raw', Timestamp('2017-04-01 12:10:00'), 2.3333333333333335]], [['sig2Raw', Timestamp('2017-04-01 12:11:00'), 2.166666666666667]], [['sig2Raw', Timestamp('2017-04-01 12:12:00'), 2.0]]]}

[[['sig1Raw', Timestamp('2017-04-01 12:00:00'), 0.0]], [['sig1Raw', Timestamp('2017-04-01 12:01:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:02:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:03:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:04:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:05:00'), 0.0]], [['sig1Raw', Timestamp('2017-04-01 12:06:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:07:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:08:00'), 0.5]], [['sig1Raw', Timestamp('2017-04-01 12:09:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:10:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:11:00'), 1.0]], [['sig1Raw', Timestamp('2017-04-01 12:12:00'), 5.0]]]


[['sig1Raw', Timestamp('2017-04-01 12:00:00'), 0.0]]
[['sig1Raw', Timestamp('2017-04-01 12:01:00'), 0.5]]
[['sig1Raw', Timestamp('2017-04-01 12:02:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:03:00'), 0.5]]
[['sig1Raw', Timestamp('2017-04-01 12:04:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:05:00'), 0.0]]
[['sig1Raw', Timestamp('2017-04-01 12:06:00'), 0.5]]
[['sig1Raw', Timestamp('2017-04-01 12:07:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:08:00'), 0.5]]
[['sig1Raw', Timestamp('2017-04-01 12:09:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:10:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:11:00'), 1.0]]
[['sig1Raw', Timestamp('2017-04-01 12:12:00'), 5.0]]



[[['sig2Raw', Timestamp('2017-04-01 12:00:00'), 2.0]], [['sig2Raw', Timestamp('2017-04-01 12:01:00'), 2.4]], [['sig2Raw', Timestamp('2017-04-01 12:02:00'), 2.8]], [['sig2Raw', Timestamp('2017-04-01 12:03:00'), 3.2]], [['sig2Raw', Timestamp('2017-04-01 12:04:00'), 3.6]], [['sig2Raw', Timestamp('2017-04-01 12:05:00'), 4.0]], [['sig2Raw', Timestamp('2017-04-01 12:06:00'), 3.0]], [['sig2Raw', Timestamp('2017-04-01 12:07:00'), 2.8333333333333335]], [['sig2Raw', Timestamp('2017-04-01 12:08:00'), 2.6666666666666665]], [['sig2Raw', Timestamp('2017-04-01 12:09:00'), 2.5]], [['sig2Raw', Timestamp('2017-04-01 12:10:00'), 2.3333333333333335]], [['sig2Raw', Timestamp('2017-04-01 12:11:00'), 2.166666666666667]], [['sig2Raw', Timestamp('2017-04-01 12:12:00'), 2.0]]]


[['sig2Raw', Timestamp('2017-04-01 12:00:00'), 2.0]]
[['sig2Raw', Timestamp('2017-04-01 12:01:00'), 2.4]]
[['sig2Raw', Timestamp('2017-04-01 12:02:00'), 2.8]]
[['sig2Raw', Timestamp('2017-04-01 12:03:00'), 3.2]]
[['sig2Raw', Timestamp('2017-04-01 12:04:00'), 3.6]]
[['sig2Raw', Timestamp('2017-04-01 12:05:00'), 4.0]]
[['sig2Raw', Timestamp('2017-04-01 12:06:00'), 3.0]]
[['sig2Raw', Timestamp('2017-04-01 12:07:00'), 2.8333333333333335]]
[['sig2Raw', Timestamp('2017-04-01 12:08:00'), 2.6666666666666665]]
[['sig2Raw', Timestamp('2017-04-01 12:09:00'), 2.5]]
[['sig2Raw', Timestamp('2017-04-01 12:10:00'), 2.3333333333333335]]
[['sig2Raw', Timestamp('2017-04-01 12:11:00'), 2.166666666666667]]
[['sig2Raw', Timestamp('2017-04-01 12:12:00'), 2.0]]

sig2 interpolated values:
[2.0, 2.4, 2.8, 3.2, 3.6, 4.0, 3.0, 2.8333333333333335, 2.6666666666666665, 2.5, 2.3333333333333335, 2.166666666666667, 2.0]


## Testing

test.py will use testDataSample to execute interpolation tests.

testSig1, testSig2, testSig3 are example inputs.




