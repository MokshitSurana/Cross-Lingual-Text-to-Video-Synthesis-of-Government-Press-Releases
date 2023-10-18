import { iArticle } from "../shared/interfaces";

// Import author profiles, just type the name you have set in _BLOG_SETUP inside the curly brackets
import { MAYUR, RUPALI } from "./_BLOG_SETUP";

// main article list to display all atricles
/**
 * Example article object
 * 
 {
    path: '/pages/tutorial/tutorial/how-to-setup-blog',
    featureArticle: true,
    preview: {
        // the author object you created in _BLOG_SETUP file
        author: MAYUR,
        date: "March 03 2022",
        articleTitle: "How to setup this plog template",
        tags: "demo, blog setup",
        thumbnail: "/images/tutorials/demo-image.jpg",
        shortIntro: "These are the steps to setup your blog",
    }
}
 */

// clear this article list and add your own
const ARTICLES_LIST: iArticle[] = [
  {
    id: "1",
    featureArticle: true,
    author: MAYUR,
    date: "September 23 2023",
    articleTitle: "PM to flag off nine Vande Bharat Express on 24th September",
    tags: ["Trains", "Chennai", "Puri", "Bhubaneswar", "Vande Bharat Express", "Connectivity", "Bharat", "Route", "Prime Minister"],
    shortIntro: "Prime Minister Shri Narendra Modi will flag off nine Vande Bharat trains on 24th September 2023 at 12:30 PM via video conferencing",
    content: `Prime Minister Shri Narendra Modi will flag off nine Vande Bharat trains on 24th September 2023 at 12:30 PM via video conferencing.

    These new Vande Bharat trains are a step towards realising Prime Minister’s vision of improving connectivity across the country and providing world class facilities to rail passengers. The new trains that will be flagged off are:
    
    Udaipur – Jaipur Vande Bharat Express
    Tirunelveli-Madurai- Chennai Vande Bharat Express
    Hyderabad –Bengaluru Vande Bharat Express
    Vijayawada – Chennai (via Renigunta) Vande Bharat Express
    Patna – Howrah Vande Bharat Express
    Kasaragod - Thiruvananthapuram Vande Bharat Express
    Rourkela - Bhubaneswar – Puri  Vande Bharat Express
    Ranchi – Howrah  Vande Bharat Express
    Jamnagar-Ahmedabad  Vande Bharat Express
     
    
    These nine trains will boost connectivity across eleven states namely Rajasthan, Tamil Nadu, Telangana, Andhra Pradesh, Karnataka, Bihar, West Bengal, Kerala, Odisha, Jharkhand and Gujarat.
    
    These Vande Bharat trains will be the fastest train along the routes of their operation and will help save considerable time of the passengers. As compared to the current fastest train along the route, Rourkela- Bhubaneswar – Puri  Vande Bharat Express and Kasaragod - Thiruvananthapuram Vande Bharat Express will be faster by about 3 hours; Hyderabad – Bengaluru Vande Bharat Express by more than 2.5 hours; Tirunelveli-Madurai- Chennai Vande Bharat Express by more than 2 hours; Ranchi – Howrah  Vande Bharat Express,  Patna – Howrah Vande Bharat Express and Jamnagar-Ahmedabad Vande Bharat Express by about 1 hour; and Udaipur - Jaipur Vande Bharat Express by about half an hour.
    
    In line with the Prime Minister’s vision to improve connectivity of important religious places across the country, Rourkela- Bhubaneswar – Puri  Vande Bharat Express and Tirunelveli-Madurai- Chennai Vande Bharat Express will connect important religious towns of Puri and Madurai. Also, the Vijayawada – Chennai Vande Bharat Express will operate via the Renigunta route and will provide connectivity to Tirupati Pilgrimage centre.
    
    The introduction of these Vande Bharat trains will herald a new standard of rail service in the country. These trains, equipped with world class amenities and advanced safety features, including Kavach technology, will be a key step towards providing modern, speedy and comfortable means of travel to common people, professionals, businessmen, student community and tourists.`,
    category: "tutorial",
  },
  {
    id: "2",
    featureArticle: true,
    author: RUPALI,
    date: "September 04 2023",
    articleTitle: "PRESIDENT OF INDIA UNVEILS 12 FEET HIGH STATUE OF MAHATMA GANDHI AND INAUGURATES GANDHI VATIKA AT GANDHI DARSHAN",
    tags: ["PRESIDENT", "Droupadi Murmu", "G20", "Tiranga", "INDIA", "MAHATMA", "GANDHI", "GANDHI", "DARSHAN"],
    // thumbnail: "/public/imp_assets/tutorials/how-to-write-first-article.svg",
    shortIntro: "The President of India, Smt Droupadi Murmu  unveiled the 12 feet high statue of Mahatma Gandhi",
    content: `The President of India, Smt Droupadi Murmu  unveiled the 12 feet high statue of Mahatma Gandhi and inaugurated ‘Gandhi Vatika’ at Gandhi Darshan, New Delhi today (September 4, 2023).

    Speaking on the occasion, the President said that Mahatma Gandhi is a boon for the entire world community. His ideals and values have given a new direction to the whole world. He showed the path of non-violence at a time when the world was suffering from many kinds of hatred and discord during the period of world wars. She added that Gandhiji's experiment with truth and non-violence gave him the status of a great human. She shared that his statues are installed in many countries and people from across the world believe in his ideals. Giving examples of Nelson Mandela, Martin Luther King Jr. and Barack Obama, she said that many great leaders considered the path of truth and non-violence shown by Gandhiji as the path of world welfare. She emphasised that by following the path shown by him, the goal of world peace can be achieved.
    
     The President said that Gandhiji laid great emphasis on sanctity in public as well as in personal life. He believed that violence can be faced through non-violence only on the basis of moral strength. She underlined that without self-confidence, one cannot act with persistence in adverse circumstances. She stated that in today's fast-changing and competitive world, there is great need for self-confidence and temperance.
    
    The President said that Gandhiji's ideals and values are very relevant for our country and society. She urged all to make efforts so that every citizen, especially the youth and children, read as much as possible about Gandhiji and imbibe his ideals. She said that the role of Gandhi Smriti and Darshan Samiti and other such institutions becomes very important in this regard. She said that they can contribute significantly in building the India of Gandhiji's dreams by making the youth and children more aware of Gandhiji's life teachings through books, films, seminars, cartoons and other media.`,
    category: "tutorial",
  },
  {
    id: "3",
    featureArticle: false,
    author: RUPALI,
    date: "September 05 2023",
    articleTitle: "PRESIDENT OF INDIA CONFERS NATIONAL AWARDS ON TEACHERS",
    tags: ["Teachers", "Elementry Education", "Award", "President", "Mental Developement"],
    // thumbnail: "/public/imp_assets/tutorials/how-to-write-first-article.svg",
    shortIntro: "The President of India, Smt Droupadi Murmu conferred National Awards on  teachers from across the country at a function held at Vigyan Bhavan, New Delhi today ",
    content: `The President of India, Smt Droupadi Murmu conferred National Awards on  teachers from across the country at a function held at Vigyan Bhavan, New Delhi today (September 5, 2023) on the occasion of Teachers’ Day.

    Speaking on the occasion, the President said that elementary education has fundamental importance in anyone's life. She added that many educationists speak about the three-H formula for the balanced development of children in which the first H is Heart, the second H is Head and the third H is Hand. She shared that heart is related to sensitivity, human values, strength of character and morality. She added that head or brain is related to mental development, reasoning power and reading and hand is related to respect for manual skills and physical labour. She said that all-round development of children would be possible only by emphasizing on such a holistic approach.
    
    The President emphasised that in view of the women participation in teaching profession, the number of female teachers receiving Teachers' awards should be higher. Encouraging female students and teachers is very important for women empowerment, she emphasized.
    
    The President said that teachers build the future of the nation. She added that quality education is considered the fundamental right of every child and role of teachers is the most important in achieving these goals. She added that the importance of teachers as nation-builders has also been clearly stated in the National Education Policy 2020.
    
    The President said that it is the duty of the teachers as well as the parents to recognize the unique abilities of each child and help the child to develop those abilities with sensitivity. She said that every parent wants their child to be given special attention and treated with affection and parents hand over their children to teachers with great trust. She added that it is a great privilege for every teacher to get the opportunity to share love among 40-50 children of a class.
    
    The President said that everyone remembers their teachers. She added that the praise, encouragement or punishment that children get from teachers remains in their memories. She said that if children are punished with the intention of improvement in them, they realize it later. She added that giving love and affection is more important than giving them knowledge.`,
    category: "tutorial",
  },
  {
    id: "4",
    featureArticle: false,
    author: RUPALI,
    date: "September 10 2023",
    articleTitle: "Prime Minister's meeting with the Prime Minister of Canada",
    tags: ["Prime Minister", "Diplomats", "G20"],
    // thumbnail: "/public/imp_assets/tutorials/how-to-write-first-article.svg",
    shortIntro: "Prime Minister met Prime Minister of Canada H.E. Mr. Justin Trudeau on 10th September on the sidelines of the G20 Summit in New Delhi",
    content: `Prime Minister met Prime Minister of Canada H.E. Mr. Justin Trudeau on 10th September on the sidelines of the G20 Summit in New Delhi.

    Prime Minister Trudeau congratulated Prime Minister on the success of India's G20 Presidency.
    
    Prime Minister highlighted that India-Canada relations are anchored in shared democratic values, respect for rule of law and strong people-to-people ties. He conveyed our strong concerns about continuing anti-India activities of extremist elements in Canada. They are promoting secessionism and inciting violence against Indian diplomats, damaging diplomatic premises, and threatening the Indian community in Canada and their places of worship. The nexus of such forces with organized crime, drug syndicates and human trafficking should be a concern for Canada as well. It is essential for the two countries to cooperate in dealing with such threats.
    
    Prime Minister also mentioned that a relationship based on mutual respect and trust is essential for the progress of India-Canada relationship.`,
    category: "tutorial",
  }
];

export const SORTED_ARTICLES_BY_DATE = ARTICLES_LIST.sort((a, b) =>
  new Date(a.date) > new Date(b.date) ? -1 : 1
);
