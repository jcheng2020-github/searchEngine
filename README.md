# searchEngine
A search engine for word space

$x$ is a $N_1$-dimension column vector represents a input sentence whoes each element is the number of a English word in the sentence.

$\phi_i$ is a $N_1$-dimension row vector represents a sentence in a corpus whoes each element is the number of a English word in the sentence.

Where $N_1$ is the number of words in vocabulary, and $N_2$ is the number of transcripts in corpus.

\begin{equation}
x \in \{a \mid 1 \leq a \leq N_1\}^N, \quad \phi_i \in \{a \mid 1 \leq a \leq N_1\}^N, \quad \forall i \in \{a \mid 1 \leq a \leq N_2\}.
\end{equation}

\begin{equation}
\Phi_z = \begin{bmatrix} 
\phi_1^T & \phi_2^T & \phi_3^T & \dots & \phi_{N_2-1}^T & \phi_{N_2}^T
\end{bmatrix}^T
\end{equation}

\begin{equation}
z = \Phi_z x
\end{equation}

Target: $$\max_{i\in \{a \mid 1 \leq a \leq N_2\}} \{z_i\} = \|z\|_\infty$$

\begin{equation}
\Phi_r = \begin{bmatrix} 
\frac{\phi_1^T}{\|\phi_1\|^2_2} & \frac{\phi_2^T}{\|\phi_2\|^2_2} & \frac{\phi_3^T}{\|\phi_3\|^2_2} & \dots & \frac{\phi_{N_2-1}^T}{\|\phi_{N_2-1}\|^2_2} & \frac{\phi_{N_2}^T}{\|\phi_{N_2}\|^2_2} 
\end{bmatrix}^T
\end{equation}

\begin{equation}
r = \Phi_r x
\end{equation}

Target: $$\max_{i\in \{a \mid 1 \leq a \leq N_2\}} \{r_i\} = \|r\|_\infty$$

\begin{equation}
\Phi_v = \begin{bmatrix} 
\frac{\phi_1^T}{\|\phi_1\|_2\|x\|_2} & \frac{\phi_2^T}{\|\phi_2\|_2\|x\|_2} & \frac{\phi_3^T}{\|\phi_3\|_2\|x\|_2} & \dots & \frac{\phi_{N_2-1}^T}{\|\phi_{N_2-1}\|_2\|x\|_2} & \frac{\phi_{N_2}^T}{\|\phi_{N_2}\|_2\|x\|_2}
\end{bmatrix}^T
\end{equation}


\begin{equation}
v = \Phi_v x
\end{equation}

Target: $$\max_{i\in \{a \mid 1 \leq a \leq N_2\}} \{v_i\} = \|v\|_\infty$$
