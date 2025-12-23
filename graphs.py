# visualizations
import matplotlib.pyplot as plt

questions = list(range(1, 21))  
accuracy_per_question = [1,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,1] 

plt.figure(figsize=(10,4))
plt.bar(questions, accuracy_per_question, color='skyblue')
plt.xlabel('Questions')
plt.ylabel('Correct (1) / Wrong (0)')
plt.title('Accuracy per Question')
plt.ylim(0,1.2)
plt.savefig('img/accuracy_per_question.png', bbox_inches='tight')
plt.show()
plt.close()

# latency visualization
latency_per_question = [1.7,1.2,0.9,1.3,0.9,1.3,1.0,1.2,1.5,0.9,1.9,0.88,0.89,1.8,0.8,0.87,1.2,1.2,1.1,1.2]
plt.figure(figsize=(10,4))
plt.plot(questions, latency_per_question, marker='o', color='orange')
plt.xlabel('Question #')
plt.ylabel('Latency (seconds)')
plt.title('Latency per Question')
plt.grid(True)
plt.savefig('img/latency_per_question.png', bbox_inches='tight')
plt.show()
plt.close()
