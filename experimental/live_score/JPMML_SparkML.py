from __future__ import print_function

import arimo.backend

from jpmml_sparkml import toPMMLBytes
from data import data


def jpmml_bytes(df, sparkMLModel):
    return toPMMLBytes(
        sc=arimo.backend.spark.sparkContext,
        df=df,
        pipelineModel=sparkMLModel)


data = data()

print(data.sdf)
data.sdf.show()


print('\nFloat-X Vector-Assembled Output:')
data.fltXVectorAssembler \
    .transform(dataset=data.sdf) \
    .show()
data.fltXVectorAssemblingPipelineModel \
    .transform(dataset=data.sdf) \
    .show()

print('Converting Float-X Vector-Assembler to PMML... ', end='')
try:
    jpmml_bytes(
        df=data.sdf,
        sparkMLModel=data.fltXVectorAssembler)
    print('done!')
except Exception as err:
    print('FAILED!')
    print(err)

print('Converting Float-X Vector-Assembling Model to PMML... ', end='')
try:
    jpmml_bytes(
        df=data.sdf,
        sparkMLModel=data.fltXVectorAssemblingPipelineModel)
    print('done!')
except Exception as err:
    print('FAILED!')
    print(err)


print('\nFloat-X Standard-Scaled Output:')
data.fltXStandardScalingPipelineModel \
    .transform(dataset=data.sdf) \
    .show()

print('Converting Float-X Standard-Scaling Model to PMML... ', end='')
try:
    jpmml_bytes(
        df=data.sdf,
        sparkMLModel=data.fltXStandardScalingPipelineModel)
    print('done!')
except Exception as err:
    print('FAILED!')
    print(err)


print('\nInt-X One-Hot-Encoded Output:')
data.intXOneHotEncodingPipelineModel \
    .transform(dataset=data.sdf) \
    .show()

print('Converting Int-X One-Hot-Encoding Model to PMML... ', end='')
try:
    jpmml_bytes(
        df=data.sdf,
        sparkMLModel=data.intXOneHotEncodingPipelineModel)
    print('done!')
except Exception as err:
    print('FAILED!')
    print(err)
