1. Input Manipulation Attack :-  A type of attack in which an attacker deliberately alters input data to mislead the model.
    As the name suggests, input manipulation attacks comprise any type of attack against an ML model that results from manipulating the input data. Typically, the result of these attacks is unexpected behavior of the ML model that deviates from the intended behavior. The impact depends highly on the concrete scenario and circumstances in which the model is used. It can range from financial and reputational damage to legal consequences or data loss.

    Many real-world input manipulation attack vectors apply small perturbations to benign input data, resulting in unexpected behavior by the ML model. In contrast, the perturbations are so small that the input looks benign to the human eye. For instance, consider a self-driving car that uses an ML-based system for image classification of road signs to detect the current speed limit, stop signs, etc. In an input manipulation attack, an attacker could add small perturbations like particularly placed dirt specks, small stickers, or graffiti to road signs. While these perturbations look harmless to the human eye, they could result in the misclassification of the sign by the ML-based system. This can have deadly consequences for passengers of the vehicle

    Research paper :- "https://arxiv.org/pdf/1707.08945".


2. Data Poisioning Attack :- Attackers inject malicous or misleading data in training dataset compromising model performance or     creating a backdoor.

    Data poisoning attacks on ML-based systems involve injecting malicious or misleading data into the training dataset to compromise the model's accuracy, performance, or behavior. As discussed before, the quality of any ML model is highly dependent on the quality of the training data. As such, these attacks can cause a model to make incorrect predictions, misclassify certain inputs, or behave unpredictably in specific scenarios. ML models often rely on large-scale, automated data collection from various sources, so they may be more susceptible to such tampering, especially when the sources are unverified or gathered from public domains.

    As an example, assume an adversary is able to inject malicious data into the training data set for a model used in antivirus software to decide whether a given binary is malware. The adversary may manipulate the training data to effectively establish a backdoor that enables them to create custom malware, which the model classifies as a benign binary.

    Research paper :- "https://arxiv.org/pdf/2408.13221"


3. Model Inversion Attack (ML03) :- Attackers train a separate model to reconstruct inputs from model outputs, potentially revealing sensitive information.

    In model inversion attacks, an adversary trains a separate ML model on the output of the target model to reconstruct information about the target model's inputs. Since the model trained by the adversary operates on the target model's output and reconstructs information about the inputs, it inverts the target model's functionality, hence the name model inversion attack.

    These attacks are particularly impactful if the input data contains sensitive information—for instance, models processing medical data, such as classifiers used in cancer detection. If an inverse model can reconstruct information about a patient's medical information based on the classifier's output, sensitive information is at risk of being leaked to the adversary. Furthermore, model inversion attacks are more challenging to execute if the target model provides less output information. For instance, successfully training an inverse model becomes much more challenging if a classification model only outputs the target class instead of every output probability.

    Research paper :- "https://arxiv.org/pdf/2311.13647"

4. Membership Inference Attack (ML04) :- Attackers analyze models behaviour to determine whether data was included in the model's training data set, potentially revealing sensitive data.

    Membership inference attacks seek to determine whether a specific data sample was included in the model's original training data set. By carefully analyzing the model's responses to different inputs, an attacker can infer which data points the model "remembers" from the training process. If a model is trained on sensitive data such as medical or financial information, this can pose serious privacy issues. This attack is especially concerning in publicly accessible or shared models, such as those in cloud-based or machine learning-as-a-service (MLaaS) environments. The success of membership inference attacks often hinges on the differences in the model's behavior when handling training versus non-training data, as models typically exhibit higher confidence or lower prediction error on samples they have seen before.

    Research Paper :- "https://arxiv.org/pdf/2402.07841"

5. Model Theft (ML05) :- Attackers train a separate model from interactions with the original model thereby stealing intellactual property.

    Model theft or model extraction attacks aim to duplicate or approximate the functionality of a target model without direct access to its underlying architecture or parameters. In these attacks, an adversary interacts with an ML model and systematically queries it to gather enough data about its decision-making behavior to duplicate the model. By observing sufficient outputs for various inputs, attackers can train their own replica model with a similar performance.

    Model theft threatens the intellectual property of organizations investing in proprietary ML models, potentially resulting in financial or reputational damage. Furthermore, model theft may expose sensitive insights embedded within the model, such as learned patterns from sensitive training data.

    Reasearch Paper :- "https://arxiv.org/pdf/2305.13584"

6. AI Supply chain attacks (ML06) -> Attackers exploit vulnerabalities in any part of ML supply chain.

    Supply chain attacks on ML-based systems target the complex, interconnected ecosystem involved in creating, deploying, and maintaining ML models. These attacks exploit vulnerabilities in any part of the ML pipeline, such as third-party data sources, libraries, or pre-trained models, to compromise the model's integrity, security, or performance. The supply chain of ML-based systems consists of more parts than traditional IT systems due to the dependence on large amounts of data. Details of supply chain attacks, including their impact, depend highly on the specific vulnerability exploited. For instance, they can result in manipulated models that perform differently than intended. The risk of supply chain attacks has grown as ML systems increasingly rely on open-source tools, publicly available datasets, and pre-trained models from external sources.

7. Transfer Learning Attack (ML07) -> Attackers manipulate the baseline model that is subsequently fine-tuned by a 3rd-party, can lead to biased or backdoored model.

    Open-source pre-trained models are used as a baseline for many ML model deployments due to the high computational cost of training models from scratch. New models are then built on top of these pre-trained models by applying additional training to fine-tune the model to the specific task it is supposed to execute. In transfer learning attacks, adversaries exploit this transfer process by manipulating the pre-trained model. Security issues such as backdoors or biases may arise if these manipulations persist in the fine-tuned model. Even if the data set used for fine-tuning is benign, malicious behavior from the pre-trained model may carry over to the final ML-based system.

8. Model Skewing (ML08) -> Attackers skews the model's behaviour for malicious purposes, (by manipulating the training dataset).

    In model skewing attacks, an adversary attempts to deliberately skew a model's output in a biased manner that favors the adversary's objectives. They can achieve this by injecting biased, misleading, or incorrect data into the training data set to influence the model's output toward maliciously biased outcomes.

    For instance, assume our previously discussed scenario of an ML model that classifies whether a given binary is malware. An adversary might be able to skew the model to classify malware as benign binaries by including incorrectly labeled training data into the training data set. In particular, an attacker might add their own malware binary with a benign label to the training data to evade detection by the trained model.

9. Output Integrity Attack :- Attacker's manipulate the model's output before processing, making it look like model produced a different output.

    If an attacker can alter the output produced by an ML-based system, they can execute an output integrity attack. This attack does not target the model itself but only the model's output. More specifically, the attacker does not manipulate the model directly but intercepts the model's output before the respective target entity processes it. They manipulate the output to make it seem like the model has produced a different output. Detection of output integrity attacks is challenging because the model often appears to function normally upon inspection, making traditional model-based security measures insufficient.

    As an example, consider the ML malware classifier again. Let us assume that the system acts based on the classifier's result and deletes all binaries from the disk if classified as malware. If an attacker can manipulate the classifier's output before the succeeding system acts, they can introduce malware by exploiting an output integrity attack. After copying their malware to the target system, the classifier will classify the binary as malicious. The attacker then manipulates the model's output to the label benign instead of malicious. Subsequently, the succeeding system does not delete the malware as it assumes the binary was not classified as malware.

10. Model Poisioning :- Attacker's manipulate the model's weights compromising model performance or creating backdoors.

    While data poisoning attacks target the model's training data and, thus, indirectly, the model's parameters, model poisoning attacks target the model's parameters directly. As such, an adversary needs access to the model parameters to execute this type of attack. Furthermore, manipulating the parameters in a targeted malicious way can be challenging. While changing model parameters arbitrarily will most certainly result in lower model performance, getting the model to deviate from its intended behavior in a deliberate way requires well-thought-out and nuanced parameter manipulations. The impact of model poisoning attacks is similar to data poisoning attacks, as it can lead to incorrect predictions, misclassification of certain inputs, or unpredictable behavior in specific scenarios.

    Research Paper :- "https://arxiv.org/pdf/2405.20975".
