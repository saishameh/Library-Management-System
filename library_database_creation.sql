create database library;
use library;

create table log_in
( SNO         int            primary key,
 NAME        varchar(20),
 PASSWORD    int);

 insert into log_in
 values ( 1, 'Reshma', '1234'),
	( 2, 'Swetha', '4321'),

create table books
( SNO         int            primary key,
 B_NAME       varchar(50) ,
 B_AUTHOR     varchar(20),
 STATUS       varchar(20));

 insert into books
 values ( 1, "Scary Stories To Tell In The Dark","Alvin Schwartz","available"),
(2,"Night Of The Living Dummy", "R.L.Stine","issued"),
(3,"Miss Peregrine's Home For Peculiar Children","Ransom Riggs","available"),
(4,"World War Z", "Max Brooks","issued"),
(5,"The Amityville Horror", "Jay Anson","available"),
(6,"Twilight", "Stephenie Meyer","issued"),
(7,"A Mosnter Calls", "Patrick Ness","available"), 
(8,"Roald Dahl Boy", "Roald Dahl","issued"),
(9,"Encylopedia Of Space", "Heather Couper","available"),
(10,"Oxford Dictionary", "John Simpson","available"),
(11,"General Knowledge 2020", "Manohar Pandey","available"),
(12,"A Game Of Thrones","George R. R. Martin","available"),
(13,"The Fellowship Of The Ring"," J. R. R. Tolkien","available"),
(14,"The Lion, the Witch and the Wardrobe","C. S. Lewis","available"),
(15,"The Colour Of Magic","Terry Pratchett","available"),
(16,"Assassin’s Apprentice"," Robin Hobb","available"),
(17,"The Lies Of Locke Lamora", "Scott Lynch","available"),
(18,"The Name Of The Wind"," Patrick Rothfuss","available"),
(19,"Dragonflight","Anne McCaffrey","available"),
(20,"To Kill A Mockingbird","Harper Lee","available"),
(21,"The Great Gatsby", "F. Scott Fitzgerald","available"),
(22,"In Cold Blood","Truman Capote","available"),
(23,"Wide Sargasso Sea","Jean Rhys","available"),
(24,"Brave New World"," Aldous Huxley","available"),
(25,"Nimona","Noelle Stevenson","available"),
(26,"This One Summer","Mariko Tamaki","available"),
(27,"Blankets","Craig Thompson","available"),
(28,"American Born Chinese","Gene Luen Yang","available"),
(29,"The Silence","Kendra Elliot","issued"),
(30,"The Silent Patient","Alex Michaelides","available"),
(31,"One By One","Ruth Ware","available"),
(32,"The Last Sister","Kendra Elliot","available"),
(33,"The Teen model mystery","Carolyn Kenne","available"),
(34,"The Arsonist","Stephanie Oakes","available"),
(35,"My Own Worst Frenemy","Kimberly Reid","available"),
(36,"Overturned","Lamar Giles","available"),
(37,"Pretty Girl-13","Liz Coley","issued"),
(38,"Grown","Tiffany D.J","available"),
(39,"And Then There Were None","Agatha Christie","issued"),
(40,"Gone Girl","Gillian Flynn","issued"),
(41,"Tinkle","Luis Fernandes","issued"),
(42,"Pride And Prejudice","Jane Austen","issued"),
(43,"Welcome To The Horrorland", "R.L.Stine","issued"),
(44,"The Diary Of A Young Girl", "Anne Frank","issued"),
(45,"Guinness World Records 2020", "Craig Glenday","issued"),
(46,"I'm Malala", "Malala Yousafzai","issued"),
(47,"Diary of A Wimpy Kid","Jeff Kinney","issued"),
(48,"Dork Diaries","Rachel Renée Russell","issued"),
(49,"The Girl On The Train","Paula Hawkins","issued");

create table student
(ROLL_NO      int      primary key,
 S_NAME      varchar(20),
 IB_NO       int,
foreign key (IB_NO)  references books(B_NO));

insert into student
values (201,"Harshida",NULL),
        (202,"Rida",NULL),
        (203,"Tanya",NULL),
        (204,"Tanisha",NULL),
        (205,"Shaheer",NULL),
        (206,"Harris",NULL),
        (207,"Yash",NULL),
        (208,"Ajey",42),
        (209,"Shlok",43),
        (210,"Lakshya",NULL),
        (211,'Rahul',40),
        (212,'Raj',41),
        (213,'Sarah',NULL),
        (214,'Sameera',48),
        (215,"Kay",49),
        (216,"Nikki",NULL),
        (217,"Taki",46),
        (218,"Sunghoon",47),
        (219,"Jay",45),
        (220,"Jake",44);
