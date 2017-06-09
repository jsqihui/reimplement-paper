# reimplement-paper
reimplement interesting papers 
How to read a paper?
1）what：要解决的问题是啥？方案是啥？
2）why： 方案sense是什么？为什么这么做有效？
3）how： 模型五要素
--输入是什么？特征X Xu，Xa，Xc，Xf
--要学习的决策函数f(x) 是什么？ f(x) = WX+b 参数量和结构决定了模型的表达能力，决定了算法信息利用率的上限
--损失函数loss(x) 是什么？ MSE，logloss etc
--求解方法是什么？ SGD，LBFGS，EM etc
--如何衡量效果？AUC，NDCG，loss
