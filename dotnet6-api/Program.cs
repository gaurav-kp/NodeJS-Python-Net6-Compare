var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/get_random", () => {
    var random = new Random();
    return new Sample{randon_number= random.Next()};
});

app.Run();

internal record Sample{
    public float randon_number {get;set;}
}