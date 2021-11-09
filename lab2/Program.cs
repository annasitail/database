using System;
using Npgsql;

namespace lab2
{

    class Mark
    {
        public int id;
        public int student_id;
        public int subject_teacher_id;
        public int mark;
    }

    class Scedule
    {
        public int id;
        public string day;
        public string time;
        public int subject_teacher_id;
        public int student_id;
    }

    class Student
    {
        public int id;
        public string name;
        public int age;
        public int grade;
    }

    class Subject
    {
        public int id;
        public string name;
        public int classes_per_semester;
    }

    class Subject_teacher
    {
        public int id;
        public int subject_id;
        public int teacher_id;
    }

    class Teacher
    {
        public int id;
        public string name;
        public int age;
        public int work_experience;
    }

    class Program
    {
        static void Main(string[] args)
        {
            // ListPhoto list = new ListPhoto();
            // Photo photo = new Photo();
            // string databaseFileName = "lab2Db.db";
            // SqliteConnection sqlite = new SqliteConnection($"Data Source={databaseFileName}");
            // PhotoRepository repository = new PhotoRepository(sqlite);

            // var cs = "Host=localhost;Username=postgres;Password=1234567890;Database=postgres";

            // var con = new NpgsqlConnection(cs);
            // con.Open();

            // var cmd = new NpgsqlCommand();
            // cmd.Connection = con;
            
            while (true)
            {
                Console.WriteLine("Enter command: ");
                string command = Console.ReadLine();
                string[] subcommand = command.Split(' ');
                int num;
                var cs = "Host=localhost;Username=postgres;Password=1234567890;Database=postgres";

                var con = new NpgsqlConnection(cs);
                con.Open();

                var sql = "SELECT version()";

                var cmd = new NpgsqlCommand(sql, con);

                var version = cmd.ExecuteScalar().ToString();
                Console.WriteLine($"PostgreSQL version: {version}");

                if (subcommand[0] == "getById")
                {
                    if (subcommand.Length < 2)
                    {
                        Console.WriteLine($"Exception: there must be number after {subcommand[0]}");
                    }
                    else if (subcommand.Length > 2)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]} {subcommand[1]}'");
                    }
                    else if (!int.TryParse(subcommand[1], out num))
                    {
                        Console.WriteLine($"Exception: enter number after {subcommand[0]}");
                    }
                    else if (int.TryParse(subcommand[1], out num))
                    {
                        // photo = repository.GetById(num);
                        // if (num <= 0)
                        // {
                        //     Console.WriteLine("Exception: entered number must be bigger, than 0");
                        // }
                        // else if (photo.id == num)
                        // {
                        //     Console.WriteLine(photo.ToString());
                        // }
                        // else 
                        // {
                        //     Console.WriteLine("Photo was not found");
                        // }
                    }
                }
                else if (subcommand[0] == "deleteById")
                {
                    if (subcommand.Length < 2)
                    {
                        Console.WriteLine($"Exception: there must be number after {subcommand[0]}");
                    }
                    else if (subcommand.Length > 2)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]} {subcommand[1]}'");
                    }
                    else if (!int.TryParse(subcommand[1], out num))
                    {
                        Console.WriteLine($"Exception: enter number after {subcommand[0]}");
                    }
                    else if (int.TryParse(subcommand[1], out num))
                    {
                        if (num <= 0)
                        {
                            Console.WriteLine("Exception: entered number must be bigger, than 0");
                        }
                        else 
                        {
                            // int count = repository.DeleteById(num);
                            // Console.WriteLine($"Number of deleted notes: {count}");
                        }
                    }
                }
                else if (subcommand[0] == "insert")
                {
                    if (subcommand.Length < 2)
                    {
                        Console.WriteLine($"Exception: there must be number after {subcommand[0]}");
                    }
                    else if (subcommand.Length > 2)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]} {subcommand[1]}'");
                    }
                    else
                    {
                        string[] splittedArray = subcommand[1].Split(',');
                        if (splittedArray.Length != 3)
                        {
                            Console.WriteLine("Exception: enter user,time,likes");
                        }
                        // else if (!Int32.TryParse(splittedArray[2], out photo.likes))
                        // {
                        //     Console.WriteLine($"Exception: there must be number after {splittedArray[1]}");
                        // }
                        else
                        {
                            // photo.user = splittedArray[0];
                            // photo.time = splittedArray[1];
                            // photo.likes = int.Parse(splittedArray[2]);
                            // long number = repository.Insert(photo);
                            // Console.WriteLine($"Index of added note: {number}");
                        } 
                    }
                }
                else if (subcommand[0] == "getTotalPages")
                {
                    if (subcommand.Length > 1)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]}'");
                    }
                    else
                    {
                        // num = repository.GetTotalPages();
                        // Console.WriteLine($"Total number of pages: {num}");
                    }
                }
                else if (subcommand[0] == "getPage")
                {
                    if (subcommand.Length < 2)
                    {
                        Console.WriteLine($"Exception: there must be number after {subcommand[0]}");
                    }
                    else if (subcommand.Length > 2)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]} {subcommand[1]}'");
                    }
                    else if (!int.TryParse(subcommand[1], out num))
                    {
                        Console.WriteLine($"Exception: enter number after {subcommand[0]}");
                    }
                    else if (int.TryParse(subcommand[1], out num))
                    {
                        if (num <= 0)
                        {
                            Console.WriteLine("Exception: entered number must be bigger, than 0");
                        }
                        else 
                        {
                            // list = repository.GetPage(num);

                            // for (int i = 0; i < 10; i++)
                            // {
                            //     Console.WriteLine(list.GetAt(i).ToString());
                            // }
                        }
                    }
                }
                else if (subcommand[0] == "export") 
                {
                    if (subcommand.Length < 2)
                    {
                        Console.WriteLine($"Exception: there must be number after {subcommand[0]}");
                    }
                    else if (subcommand.Length > 2)
                    {
                        Console.WriteLine($"Exception: do not enter anything after '{subcommand[0]} {subcommand[1]}'");
                    }
                    else if (int.TryParse(subcommand[1], out num))
                    {
                        Console.WriteLine($"Exception: enter string after {subcommand[0]}");
                    }
                    else if (!int.TryParse(subcommand[1], out num))
                    {
                        // string value = subcommand[1];
                        // list = repository.GetExport(value);

                        //

                        //Console.WriteLine($"Name of created file: './NewFile.csv' \nNumber of exported lines: {list.GetCount()}");
                    }
                }
                else if (subcommand[0] == "exit")
                {
                    break;
                }
                else if (subcommand[0] == null)
                {
                    Console.WriteLine("Exception: enter command, please");
                }
                else 
                {
                    Console.WriteLine("Exception: unknown command");
                }
            }
        }
    }
}
