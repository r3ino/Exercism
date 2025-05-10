public static class LogAnalysis 
{
    // TODO: define the 'SubstringAfter()' extension method on the `string` type
    public static string SubstringAfter(this string str, string delemiter) => str.Split(delemiter)[1];
    // TODO: define the 'SubstringBetween()' extension method on the `string` type
    public static string SubstringBetween(this string str, string start, string end) => str.Split(start)[1].Split(end)[0];
    // TODO: define the 'Message()' extension method on the `string` type
    public static string Message(this string logLine) => logLine.SubstringAfter(": ");
    // TODO: define the 'LogLevel()' extension method on the `string` type
    public static string LogLevel(this string logLine) => logLine.SubstringBetween("[","]");
}