# Classification by Backpropagation (Neural Networks)

**Backpropagation** (Backward Propagation of Errors) is the fundamental algorithm that allows Artificial Neural Networks to learn. It is a mathematically rigorous way of telling each neuron in a network how much "blame" it carries for an incorrect prediction, and exactly how it should change to improve next time.

---

## 1. Architecture of the Learning Engine
An Artificial Neural Network (ANN) consists of interconnected layers of "neurons." Each connection has a **Weight ($w$)** and each neuron has a **Bias ($b$)**.

* **Input Layer:** Represents the features of your data ($x_1, x_2, \dots, x_n$).
* **Hidden Layers:** Where features are combined into complex patterns. Backpropagation is primarily concerned with updating the weights in these layers.
* **Output Layer:** The final prediction ($\hat{y}$).

![ann_architecture](./imgs/ann_architecture.jpg)

### **Anatomy of a Single Neuron**

Each neuron performs two operations:

**1. Linear combination (weighted sum):**
$$z = \sum_{i=1}^{n} w_i x_i + b = \mathbf{w}^T \mathbf{x} + b$$

**2. Non-linear activation:**
$$a = f(z)$$

Where $f$ is the activation function. Without activation functions, stacking many layers would still produce only a linear model.

### **Network Notation**

| Symbol | Meaning |
|:---|:---|
| $L$ | Total number of layers |
| $n^{[l]}$ | Number of neurons in layer $l$ |
| $W^{[l]}$ | Weight matrix of layer $l$ (shape: $n^{[l]} \times n^{[l-1]}$) |
| $b^{[l]}$ | Bias vector of layer $l$ (shape: $n^{[l]} \times 1$) |
| $a^{[l]}$ | Activation output of layer $l$ |
| $z^{[l]}$ | Pre-activation (linear) output of layer $l$ |

---

## 2. Activation Functions

Activation functions introduce **non-linearity**, allowing neural networks to learn complex patterns.

### **A. Sigmoid**
$$\sigma(z) = \frac{1}{1 + e^{-z}} \qquad \text{Range: } (0, 1)$$

* **Use:** Output layer for binary classification.
* **Problem:** Vanishing gradient — saturates at extremes, gradients ≈ 0.

### **B. Tanh (Hyperbolic Tangent)**
$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} \qquad \text{Range: } (-1, 1)$$

* **Use:** Hidden layers (zero-centred, better than sigmoid).
* **Problem:** Still suffers from vanishing gradient at extremes.

### **C. ReLU (Rectified Linear Unit)**
$$\text{ReLU}(z) = \max(0, z) \qquad \text{Range: } [0, \infty)$$

* **Use:** Default for hidden layers in deep networks.
* **Problem:** "Dying ReLU" — neurons that output 0 stop learning permanently.

### **D. Leaky ReLU**
$$\text{LeakyReLU}(z) = \begin{cases} z & z > 0 \\ \alpha z & z \leq 0 \end{cases} \qquad \text{(typically } \alpha = 0.01\text{)}$$

* **Use:** Fix for dying ReLU — small negative slope keeps gradients alive.

### **E. Softmax (Output Layer — Multi-class)**
$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^{k} e^{z_j}}$$

* **Use:** Output layer when classifying into $k > 2$ classes.
* Converts raw scores into a **probability distribution** that sums to 1.

### **Activation Function Comparison**

| Function | Range | Gradient Vanishes? | Best Used In |
|:---|:---|:---|:---|
| Sigmoid | (0, 1) | Yes (extremes) | Binary output layer |
| Tanh | (-1, 1) | Yes (extremes) | Hidden layers (shallow nets) |
| ReLU | [0, ∞) | No (positive side) | Hidden layers (deep nets) |
| Leaky ReLU | (-∞, ∞) | No | Hidden layers (dying ReLU fix) |
| Softmax | (0, 1) each | — | Multi-class output layer |

---

## 3. The Cycle of Learning: Forward & Backward

### **Phase 1: Forward Propagation (The Prediction)**
The network takes the input and passes it through the layers. At each neuron, we calculate a weighted sum:
$$z = \sum (weight \times input) + bias$$
Then, an **Activation Function** $f(z)$ is applied to produce the output for that neuron. This continues until the output layer generates a prediction.

**Vectorised form for layer $l$:**
$$z^{[l]} = W^{[l]} a^{[l-1]} + b^{[l]}$$
$$a^{[l]} = f(z^{[l]})$$

### **Phase 2: Calculating the Loss (The Error)**
We compare the prediction ($\hat{y}$) with the actual target ($y$) using a **Loss Function**.

**Mean Squared Error (Regression):**
$$\mathcal{L}_{MSE} = \frac{1}{2}(y - \hat{y})^2$$

**Binary Cross-Entropy (Binary Classification):**
$$\mathcal{L}_{BCE} = -[y \log \hat{y} + (1-y)\log(1-\hat{y})]$$

**Categorical Cross-Entropy (Multi-class):**
$$\mathcal{L}_{CCE} = -\sum_{k=1}^{K} y_k \log \hat{y}_k$$

### **Phase 3: Backward Propagation (The Correction)**
This is the core of the algorithm. We use the **Chain Rule of Calculus** to calculate the gradient of the loss function with respect to each weight.
* We go backward from the output layer to the input layer.
* We calculate how much a tiny change in a specific weight would change the final error.


### **The Chain Rule — Why It Works**

The loss $\mathcal{L}$ depends on the weight $w$ through a chain of intermediate values:
$$\mathcal{L} \rightarrow \hat{y} \rightarrow z \rightarrow w$$

By the Chain Rule:
$$\frac{\partial \mathcal{L}}{\partial w} = \frac{\partial \mathcal{L}}{\partial \hat{y}} \cdot \frac{\partial \hat{y}}{\partial z} \cdot \frac{\partial z}{\partial w}$$

Each term is computed separately and multiplied together. This is why it is called **backpropagation** — we propagate these partial derivatives backwards through the network.

---

## 4. The Weight Update Rule (Gradient Descent)
Once the "error gradient" is calculated, we update the weight using the following formula:
$$w_{new} = w_{old} - \eta \times \frac{\partial \mathcal{L}}{\partial w}$$

* **$\frac{\partial \mathcal{L}}{\partial w}$:** The gradient (direction of steepest increase in error).
* **$\eta$ (Learning Rate):** A small positive number (e.g., 0.01) that controls the size of the update step.

### **Effect of Learning Rate**

| Learning Rate | Behaviour | Risk |
|:---|:---|:---|
| Too large ($\eta > 0.1$) | Big steps — fast but unstable | Overshooting the minimum; divergence |
| Too small ($\eta < 0.0001$) | Tiny steps — stable but slow | Very slow convergence |
| Just right | Smooth descent toward minimum | Optimal learning |

### **Variants of Gradient Descent**

| Variant | Uses Per Update | Speed | Stability |
|:---|:---|:---|:---|
| **Batch GD** | All training samples | Slow | Very stable |
| **Stochastic GD (SGD)** | 1 sample at a time | Fast | Noisy/unstable |
| **Mini-Batch GD** | $k$ samples (e.g., 32, 64) | Balanced | Balanced |

**Mini-Batch GD** is the most commonly used in practice as it balances speed and stability.

### **Advanced Optimizers**

| Optimizer | Key Idea | Advantage |
|:---|:---|:---|
| **Momentum** | Accumulates velocity in the gradient direction | Escapes local minima faster |
| **AdaGrad** | Adapts learning rate per parameter | Good for sparse data |
| **RMSprop** | Decaying average of squared gradients | Stable for RNNs |
| **Adam** | Combines Momentum + RMSprop | Default choice for most problems |

---

## 5. Key Terminology for Students

| Term | Definition |
| :--- | :--- |
| **Epoch** | One complete pass of the entire training dataset through the network. |
| **Batch Size** | Number of training samples processed before updating weights. |
| **Activation Function** | Introduces non-linearity (e.g., **Sigmoid**, **ReLU**, **Tanh**). Without this, the network is just a simple linear model. |
| **Vanishing Gradient** | A problem where gradients become so small that the weights in early layers stop updating, effectively "stalling" the learning. |
| **Exploding Gradient** | The opposite — gradients grow too large, causing unstable weight updates. Fixed by **gradient clipping**. |
| **Convergence** | The point where the error reaches a minimum and additional training doesn't improve the model. |
| **Dropout** | Randomly disabling a fraction of neurons during training to prevent overfitting. |
| **Early Stopping** | Halting training when validation error stops improving, to prevent overfitting. |
| **Weight Initialization** | Setting initial weights to small random values (e.g., Xavier/He initialization) to prevent vanishing/exploding gradients at the start. |


---

## 6. The Vanishing Gradient Problem — In Depth

The vanishing gradient is one of the most critical challenges in deep learning.

**Why it happens:**
* Sigmoid and Tanh derivatives are always $\leq 0.25$ and $\leq 1.0$ respectively.
* The chain rule **multiplies** these derivatives layer by layer going backward.
* With many layers: $0.25 \times 0.25 \times 0.25 \times \ldots \approx 0$ very quickly.

**Effect:** Early layers receive near-zero gradients → weights don't update → those layers don't learn.

**Solutions:**

| Solution | How It Helps |
|:---|:---|
| **Use ReLU** | Gradient = 1 for positive inputs → no vanishing |
| **Batch Normalization** | Normalizes layer inputs → keeps gradients in healthy range |
| **Residual Connections (ResNets)** | Skip connections allow gradient to flow directly |
| **Better initialization (Xavier/He)** | Scales initial weights to avoid saturation from the start |
| **Gradient clipping** | Caps gradient magnitude to prevent both vanishing and explosion |

---

## 7. Regularization: Preventing Overfitting in Neural Networks

| Technique | How It Works | Effect |
|:---|:---|:---|
| **L2 Regularization (Weight Decay)** | Adds $\lambda \sum w^2$ to the loss | Penalises large weights; shrinks them toward 0 |
| **L1 Regularization** | Adds $\lambda \sum \|w\|$ to the loss | Encourages sparse weights (some become exactly 0) |
| **Dropout** | Randomly sets neuron outputs to 0 during training | Forces network to learn redundant representations |
| **Early Stopping** | Stop training when validation loss stops decreasing | Prevents memorizing training noise |
| **Data Augmentation** | Artificially increases training data | Reduces overfitting by exposing more variation |

**Dropout formula:** During training, each neuron is kept with probability $p$ (typically 0.5–0.8). At test time, all neurons are active but outputs are scaled by $p$.

---

## 8. Strengths and Practical Challenges

### **The Strengths**
* **Universal Approximator:** Mathematically, a neural network with enough hidden layers can learn *any* function.
* **Feature Learning:** Unlike Decision Trees, you don't need to tell a Neural Network which features are important; it discovers them automatically through Backpropagation.
* **Scales with Data:** Performance keeps improving as more training data is added, unlike many classical algorithms.

### **The Challenges**
* **Local Minima:** The algorithm might get "stuck" in a small dip in the error curve rather than finding the absolute lowest point (Global Minimum).
* **Overfitting:** ANNs are so powerful they can "memorize" noise. Techniques like **Dropout** or **Early Stopping** are used to prevent this.
* **Data Hunger:** Backpropagation generally requires thousands of labeled examples to reach high accuracy.
* **Hyperparameter Tuning:** Number of layers, neurons, learning rate, batch size — each requires careful tuning.
* **Interpretability:** Unlike Decision Trees, it is extremely difficult to explain *why* a neural network made a specific prediction.

---

## 9. Real-World Applications
1.  **Handwriting Recognition:** Converting scanned handwritten text into digital characters (The famous MNIST dataset).
2.  **Autonomous Vehicles:** Processing camera feeds in real-time to identify pedestrians and traffic lights.
3.  **Language Translation:** Modern systems (like Google Translate) use deep backpropagation-based networks to understand context between languages.
4.  **Face ID:** Identifying unique facial landmarks to unlock smartphones.
5.  **Medical Imaging:** Detecting tumours in X-rays and MRI scans with radiologist-level accuracy.
6.  **Speech Recognition:** Converting spoken language to text (Siri, Google Assistant, Alexa).
7.  **Drug Discovery:** Predicting the molecular properties of new compounds in pharmaceutical research.
8.  **Financial Fraud Detection:** Detecting anomalous transaction patterns in real time.

---

## 10. Comparison: How does it differ from previous topics?

| Feature | Naive Bayes | Decision Trees | Backpropagation |
| :--- | :--- | :--- | :--- |
| **Structure** | Probabilistic counts | Hierarchical splits | Layered Neurons |
| **Non-Linearity** | Limited | High | Extremely High |
| **Transparency** | Clear math | Very clear (Visual) | "Black Box" (Hidden) |
| **Training Time** | Seconds | Minutes | Hours/Days |
| **Data Required** | Small to Medium | Small to Medium | Large (thousands+) |
| **Feature Engineering** | Manual | Manual | Automatic |
| **Handles Images/Audio** | Poor | Poor | Excellent |
| **Overfitting Risk** | Low | Medium | High (needs regularization) |

---

# Algorithm: Backpropagation (Neural Networks)

Backpropagation is an iterative gradient descent algorithm used to train Artificial Neural Networks. It works by calculating the error at the output layer and propagating it backward through the network to update the weights and minimize the error.

![backprop](./imgs/backprop.webp)

---

## 1. Basic Working Steps
1.  **Initialize Weights:** Assign small random numbers to all weights and biases in the network.
2.  **Feed-Forward:** Pass the input through the network (Input → Hidden → Output) using activation functions to generate a prediction.
3.  **Calculate Error:** Compare the predicted output with the actual target value using a loss function (like Mean Squared Error).
4.  **Backward Pass:** Calculate the gradient of the error with respect to each weight by moving backward from the output layer to the hidden layer.
5.  **Update Weights:** Adjust the weights and biases using the learning rate to reduce the error.
6.  **Repeat:** Iterate through many epochs until the error is sufficiently small.

---

## 2. Key Formulas

### **A. Output of a Neuron**
For a neuron $j$, the net input $I_j$ is:
$$I_j = \sum w_{ij}O_i + \theta_j$$
The output $O_j$ is calculated using the **Sigmoid Activation Function**:
$$O_j = \frac{1}{1 + e^{-I_j}}$$

### **B. Error Calculation (Output Layer)**
The error ($\text{Err}_j$) for an output unit $j$ is:
$$\text{Err}_j = O_j(1 - O_j)(T_j - O_j)$$
* $T_j$ = Target value, $O_j$ = Actual output.
* The term $O_j(1 - O_j)$ is the **derivative of the sigmoid function** — this is where the chain rule appears.

### **C. Error for Hidden Layer Neurons**
For a hidden neuron $j$, the error depends on the errors of all downstream output neurons:
$$\text{Err}_j = O_j(1 - O_j) \sum_k w_{jk} \cdot \text{Err}_k$$

This is the "backward propagation" — error flows from output → hidden → input.

### **D. Weight Update**
The change in weight ($\Delta w_{ij}$) is calculated as:
$$\Delta w_{ij} = l \cdot \text{Err}_j \cdot O_i$$
* $l$ = Learning rate.

### **E. Weight Update with Momentum**
To accelerate convergence and escape local minima, momentum $\mu$ is added:
$$\Delta w_{ij}(t) = l \cdot \text{Err}_j \cdot O_i + \mu \cdot \Delta w_{ij}(t-1)$$


---

## 3. Practical Example

**Scenario: A simple network with 1 Input ($I=1$), 1 Hidden Neuron, and 1 Output.**
* Assume current Output $O_{out} = 0.6$
* Target Output $T = 0.9$
* Learning Rate $l = 0.1$

### **Step 1: Calculate Output Error**
$$\text{Err}_{out} = O_{out}(1 - O_{out})(T - O_{out})$$
$$\text{Err}_{out} = 0.6 \times (1 - 0.6) \times (0.9 - 0.6)$$
$$\text{Err}_{out} = 0.6 \times 0.4 \times 0.3 = \mathbf{0.072}$$

### **Step 2: Update Weight between Hidden and Output Layer**
Assume the hidden neuron output $O_{hidden} = 0.5$ and initial weight $w = 0.4$.
$$\Delta w = (0.1) \times 0.072 \times 0.5 = 0.0036$$
$$\text{New Weight} = 0.4 + 0.0036 = \mathbf{0.4036}$$

**Decision:** The weight is slightly increased to push the actual output (0.6) closer to the target (0.9).

### **Step 3: Propagate Error to Hidden Layer**
Assume weight between input and hidden neuron $w_{in \to h} = 0.6$ and $O_{hidden} = 0.5$, $O_{input} = 1.0$.
$$\text{Err}_{hidden} = O_{hidden}(1 - O_{hidden}) \times w_{h \to out} \times \text{Err}_{out}$$
$$\text{Err}_{hidden} = 0.5 \times 0.5 \times 0.4 \times 0.072 = \mathbf{0.0072}$$

$$\Delta w_{in \to h} = 0.1 \times 0.0072 \times 1.0 = 0.00072$$
$$\text{New Weight}_{in \to h} = 0.6 + 0.00072 = \mathbf{0.60072}$$

### **Tracking Progress Over Epochs**

| Epoch | Output | Error | $\Delta w$ |
|:---|:---|:---|:---|
| 1 | 0.600 | 0.072 | +0.0036 |
| 2 | ~0.604 | ~0.068 | +0.0034 |
| 5 | ~0.620 | ~0.055 | ~0.0027 |
| 20 | ~0.750 | ~0.020 | ~0.0010 |
| 50 | ~0.880 | ~0.003 | ~0.0001 |

With each epoch, the error shrinks and the weight updates become smaller as the network converges toward the target.

---

## 4. Python Implementation

```python
import numpy as np

# --- Activation functions ---
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(a):
    return a * (1 - a)   # derivative of sigmoid w.r.t. z, given output a

def relu(z):
    return np.maximum(0, z)

def relu_derivative(z):
    return (z > 0).astype(float)

# --- Simple 2-layer network (1 hidden layer) ---
class SimpleNN:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        # Xavier initialization
        self.W1 = np.random.randn(hidden_size, input_size) * np.sqrt(1/input_size)
        self.b1 = np.zeros((hidden_size, 1))
        self.W2 = np.random.randn(output_size, hidden_size) * np.sqrt(1/hidden_size)
        self.b2 = np.zeros((output_size, 1))
        self.lr = lr

    def forward(self, X):
        # Hidden layer
        self.z1 = self.W1 @ X + self.b1
        self.a1 = sigmoid(self.z1)
        # Output layer
        self.z2 = self.W2 @ self.a1 + self.b2
        self.a2 = sigmoid(self.z2)
        return self.a2

    def backward(self, X, y):
        m = X.shape[1]   # number of samples

        # Output layer gradients
        dz2 = self.a2 - y                            # for MSE + sigmoid
        dW2 = (1/m) * dz2 @ self.a1.T
        db2 = (1/m) * np.sum(dz2, axis=1, keepdims=True)

        # Hidden layer gradients (chain rule)
        da1 = self.W2.T @ dz2
        dz1 = da1 * sigmoid_derivative(self.a1)
        dW1 = (1/m) * dz1 @ X.T
        db1 = (1/m) * np.sum(dz1, axis=1, keepdims=True)

        # Weight updates
        self.W2 -= self.lr * dW2
        self.b2 -= self.lr * db2
        self.W1 -= self.lr * dW1
        self.b1 -= self.lr * db1

    def train(self, X, y, epochs=1000):
        losses = []
        for epoch in range(epochs):
            y_hat = self.forward(X)
            loss  = np.mean((y - y_hat) ** 2)
            losses.append(loss)
            self.backward(X, y)
            if epoch % 100 == 0:
                print(f"Epoch {epoch:4d} | Loss: {loss:.6f}")
        return losses

# --- Usage ---
# X shape: (features, samples), y shape: (1, samples)
# nn = SimpleNN(input_size=2, hidden_size=4, output_size=1, lr=0.1)
# losses = nn.train(X_train, y_train, epochs=500)
```

---

## 5. Quick Reference Summary

| Concept | Formula | Purpose |
|:---|:---|:---|
| Neuron output | $z = \mathbf{w}^T\mathbf{x} + b,\ a = f(z)$ | Forward pass |
| Sigmoid | $\sigma(z) = \frac{1}{1+e^{-z}}$ | Smooth 0–1 output |
| ReLU | $\max(0, z)$ | Fast hidden layer activation |
| MSE Loss | $\frac{1}{2}(y - \hat{y})^2$ | Regression error |
| Cross-Entropy | $-y\log\hat{y} - (1-y)\log(1-\hat{y})$ | Classification error |
| Output error | $\text{Err}_j = O_j(1-O_j)(T_j - O_j)$ | Delta at output |
| Hidden error | $\text{Err}_j = O_j(1-O_j)\sum_k w_{jk}\text{Err}_k$ | Backpropagated delta |
| Weight update | $w \leftarrow w + l \cdot \text{Err}_j \cdot O_i$ | Gradient descent step |
| With momentum | $\Delta w(t) = l \cdot \text{Err}_j \cdot O_i + \mu\Delta w(t-1)$ | Faster convergence |