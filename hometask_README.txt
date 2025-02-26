**Q1. What Happened before and After Interrupt? when Run code without interrupts?**

	"I didn't notice or observed anything unusual during the execution of code without interrupts but the button functionality
	was not working properly and it wasn't contributing in turning on and off the display."


**Q2. What is a debounce issue and how to get rid of it ?**

	"It is the generation of multiple signals on pressing the button which is caused due to multiple and rapid vibaration of metals of button
	and hardware. It leads to generation of noise along with one stable state.
	We can use debounce delay and timing filters to address this issue.
	The debounce delay concept works in a way that it ignores the rapid on/off of switch and registers only stable state. "


**Q3. where debounce is dangerous IF it is not addressed?**

	"The debounce can be very dangerous and catastrophic in systems like infusion pumps and like insuling ejection pumps in which multiple 
	signals can lead to the over dosages of the medicine.
	In systems like automotive cars if debounce is not handled like gear changing and break pressing then It can cause unwanted and multiple
	gear switching and mutiple brakes and cause accidents."


**Q4. why debounce occurs? is it a compiler error? logical error or microcontroller is cheap?**

	"Debounce is neither a compiler or logical error and nor the issue is that the microcontroller is chaep. It is the harware and mechanical component
	ISSUE which arises becuase there is no instant connection of metals on pressing the button. So multiple signals and noise is generated."


**Q5. why do we use interrupts?
	
	"We use interrupts to handle time-sensitive tasks without continuously checking (polling) for events, making the system more efficient. 
	They allow the microcontroller to respond instantly to external events (e.g., button presses, sensor signals) while performing other tasks.
 	This improves real-time performance and reduces CPU usage in embedded systems."


**Q6. how does interrupt lower processing cost of microcontrollers?**

	"Interrupts lower processing cost by eliminating the need for constant polling, where the CPU repeatedly checks for events.
	 Instead, the microcontroller can stay idle or execute other tasks until an interrupt occurs, reducing unnecessary power consumption and CPU usage.
 	This makes real-time responses faster and more efficient without wasting processing resources."
	


	