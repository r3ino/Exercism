class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
    public int ExpectedMinutesInOven() => 40;

    // TODO: define the 'RemainingMinutesInOven()' method
    public int RemainingMinutesInOven(int iInOvenTime) => ExpectedMinutesInOven() - iInOvenTime;
    
    // TODO: define the 'PreparationTimeInMinutes()' method
    public int PreparationTimeInMinutes(int iNumberOfLayers) => iNumberOfLayers * 2;

    // TODO: define the 'ElapsedTimeInMinutes()' method
    public int ElapsedTimeInMinutes(int iNumberOfLayers, int iInOvenTime) => iNumberOfLayers * 2 + iInOvenTime;
}
