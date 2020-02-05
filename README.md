Variant of Texygen created by Nicolas Pingal for MQP paper link here. More arguments have been added and some functionality has been implemented.
```bash
#usage:
python main.py -g <GAN type> -t <training method> -d <data location> -o <output path> -p <pre-training epochs> -a <adversarial training epochs> -c <csv output>
  -g <GAN type>
    specify the GAN type in the experiment
    <GAN type> = seqgan | maligan | rankgan | leakgan | gsgan | textgan | mle
  -t <training method>
    specify the traning method in the experiment
    <training method> = oracle | cfg | real
    default is oracle
  -d <data location>
    use user\'s own dataset
    only available with real data training
    default is 'data/image_coco.txt'
  -o <output path>
    specify the output path for the test file generated
    default is 'save/test_file.txt'
  -p <pre-training epochs>
    specify the number of pre-training epochs
    default is 80
  -a <adversarial training epochs>
    specify the number of adversarial training epochs
    default is 100
  -c <csv output>
    specify the csv output path
    default is (gan type)-experiment-log.csv
```

## Requirement
We suggest you run the platform under Python 3.6+ with following libs:
* **TensorFlow >= 1.5.0**
* Numpy 1.12.1
* Scipy 0.19.0
* NLTK 3.2.3
* CUDA 7.5+ (Suggested for GPU speed up, not compulsory)    

Or just type `pip install -r requirements.txt` in your terminal.

## Implemented Models and Original Papers

* **Texygen** - [Texygen: A Benchmarking Platform for Text Generation Models](https://arxiv.org/abs/1802.01886)

* **SeqGAN** -  [SeqGAN: Sequence Generative Adversarial Nets with Policy Gradient](https://arxiv.org/abs/1609.05473)

* **MaliGAN** - [Maximum-Likelihood Augmented Discrete Generative Adversarial Networks](https://arxiv.org/abs/1702.07983)

* **RankGAN** - [Adversarial ranking for language generation](http://papers.nips.cc/paper/6908-adversarial-ranking-for-language-generation)

* **LeakGAN** - [Long Text Generation via Adversarial Training with Leaked Information](https://arxiv.org/abs/1709.08624)

* **TextGAN** - [Adversarial Feature Matching for Text Generation](https://arxiv.org/abs/1706.03850)
 
* **GSGAN** - [GANS for Sequences of Discrete Elements with the Gumbel-softmax Distribution](https://arxiv.org/abs/1611.04051)


