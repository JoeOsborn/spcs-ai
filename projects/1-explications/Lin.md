The AI system I'm describing is developed by [Microsoft China](http://microsoft.com/). It is a game called ***小冰读心术*** *(or in English, **Mind Reader**)* and it utilizes **Decision Trees** as its main algorithm. 

Here is how one plays the game: 
1. Consider a famous person in your mind
2. The AI will ask you 15 questions about this famous person, such as *Does this person have black hair or blonde hair?*
3. You can either respond the question or select *I don't know*
4. Based on the responses, the AI guesses who this famous person is

This project is based on a decision tree model, but the complicated part is the data gathering behind the scenes. Microsoft must have utilized natural language processing technologies to gather the facts and datas about the famous people, and in order to do that, they have crawled and processed millions of web pages with their **Bing** search technologies. After processing the facts collected from the internet, translating them into formatted data and storing them in databases, the data can finally go through the decision tree each time a user begins a game session. In my personal opinion, the data collection is the challenging part.

The only way of interaction this game has with its users is the 15 questions. And because it doesn't seem to be able to learn from its users, abusing or misusing the system is unlikely to cause damage to it or to other users (unless a web hack/exploit takes place). In its current state, this game has limited uses; people can only use it to poke fun. However, the same technology could be used for various purposes in the future; for example, automated chat bots or customer services, or any other tasks that can be categorized into a similar computational model. 