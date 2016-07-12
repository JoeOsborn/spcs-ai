The AI system I'm describing is developed by [Microsoft China](http://microsoft.com/). It is a game called **_小冰读心术_** _(or in English, **Mind Reader**)_ and it utilizes __Decision Trees__ as its main algorithm. 

Here is how one plays the game: 
> 1. Consider a famous person in your mind
> 2. The AI will ask you 15 multiple-choice questions about this famous person, such as *Does this person have black hair or blonde hair?*
> 3. You can either respond the question or select *I don't know*
> 4. Based on the responses, the AI guesses who this famous person is

This project is based on a decision tree model, but the complicated part is the data gathering behind the scenes. Microsoft must have utilized natural language processing technologies to gather the facts and datas about the famous people, and in order to do that, they have crawled and processed millions of web pages with their __Bing__ search technologies. After processing the facts collected from the internet, translating them into formatted data and storing them in a database, the data can finally go through the decision tree each time a user begins a game session. *(In my personal opinion, the data collection is the most challenging part.)*

The only way of interaction with its users this game allows is the 15 multiple-choice questions. And because it is not designed to learn from its users, abusing or misusing the system *(e.g. providing it with strange inputs)* is unlikely to cause damage to it or to other users *(unless a web hack/exploit takes place)*. In its current state, this game has only limited uses; users can only use it to poke fun, kill time and relax. However, the same technology could be used for various purposes in the future; for example, automated chat bots or customer services, or any other tasks that can be categorized into a similar computational model. 