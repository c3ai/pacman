var main = require(process.argv[3]);

describe( "pacman", function () {
    var arrayEquality = function(first, second){
        count = 0;
        for (i = 0; i < second.length; i++) {
            if(parseInt(second[i]) == parseInt(first[i])){
                count = count + 1;
            }
        }
        return (count == 3);
    }
    beforeEach(function () {
        jasmine.addCustomEqualityTester(arrayEquality);
    });

    it("traverses borders.txt", function () {
        expect(main.pacman("borders.txt")).toEqual([9,0,19]);
    });

    it("traverses walls.txt", function () {
        expect(main.pacman("walls.txt")).toEqual([4,6,8]);
    });

    it("traverses generic.txt", function () {
        expect(main.pacman("generic.txt")).toEqual([6,1,27]);
    });

    it("doesn't run for initialPosition1.txt", function () {
        expect(main.pacman("initialPosition1.txt")).toEqual([-1,-1,0]);
    });

    it("doesn't run for initialPosition2.txt", function () {
        expect(main.pacman("initialPosition2.txt")).toEqual([-1,-1,0]);
    });

    // it("traverses generated.txt", function () {
    //     expect(main.pacman("generated.txt").toEqual([14869,4926,894]));
    // });

    it("traverses generated-smaller.txt", function () {
        expect(main.pacman("generated-smaller.txt")).toEqual([2142,147,148]);
    });
});
