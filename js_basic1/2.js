function clicked1() {
    // 변수(variable) 선언 (=초기화 initializing)

    /* 
        변수의 선언은 두가지 방법이 있다.

        1. let 변수. 배열변수 중에서도 크기가 변하는 변수
        1. const 상수. 배열이 아닌 모든 변수(배열이어도 크기가 변하지 않는 배열은 const 사용)
        1. var 변수. let과 동일하다. 2015년의 js는 var만 쓸 수 있었다. 요즘은 let과 const만 쓴다.

        const를 쓰는 이유: 가끔 변수의 값을 바꾸고 싶지 않을 때가 있다.
        만일 1000라인의 js코드를 가지고 있고, 어떤 이름의 변수를 사용한다면,
        그때 동일한 변수를 그 안에서 실수로 업데이트해버린다면,
        문제가 발생했을 때 추적이 불가능해서, 나쁜 일이 발생할 것이다.
        그래서 상수로 바꾸지 않게 하는 것이다.

    */

    let n1 = 1
    let n2 = 2
    let n3 = 3
    // const n1 = 1 // ***
    // const n2 = 2 // ***
    // const n3 = 3 // ***
    // alert(n1) // ***
    // alert(n2) // ***
    // alert(n3) // ***








    // 변수 업데이트

    /* 
        1. let은 업데이트가 가능하다. 
        1. const는 업데이트가 불가능하므로 에러가 뜰 것이다.
    */

    n1 = 2
    n2 = 3
    n3 = 4
    // alert(n1) // ***
    // alert(n2) // ***








    // 변수의 타입

    /*
        Number 숫자 : 1 2 3 // 아이템중 하나
        Float 실수 : 0.1 2.0 // 아이템중 하나
        String 문자열 '' // 아이템중 하나
        Boolean 논리 : true, false // 아이템중 하나. 보통 변수앞에 is를 붙여서 쓴다. 예를 들어, "isLogin = true"이면 "로그인을 했는지의 여부 = 로그인했음" 이런 느낌이다.
        Object 오브젝트 : {1, 2, 3} // 라벨형 상자 (상자 안에 아이템뿐만 아니라 상자도 들어감)
        Array 어레이 : [1, 2, 3] // 나열형 상자 (상자 안에 아이템뿐만 아니라 상자도 들어감)
        Set 세트 : Set {1, 2, 3} // 콜렉션
    */

    const s1 = '1'
    const s2 = '2'
    const b1 = n1 < n2
    const b2 = n1 === n2
    // alert(n1 + n2) // 3 // ***
    // alert(s1 + s2) // 12 // ***
    // alert(b1) // ***
    // alert(b2) // ***





    






    // 콘솔로그의 사용

    /*
        현장에서는 아래와 같은 형태로 변수의 값을 확인하면서 작업한다. 
        이제부터는 변수 확인에 alert() 대신 console.log() 메소드를 사용해서 진행하겠다.
     */

    // console.log(s1) // ***
    // console.log(s2) // ***













    // 오브젝트

    /*
        오브젝트는 객체라고도 불린다.
        오브젝트는 키와 밸류로 된 값이다. 
        오브젝트 전체를 꺼내기도 하지만, 실제 밸류값을 꺼내려면 어떤 키에서 꺼낼 지를 지정해줘야한다.
        하나의 객체에 여러 변수를 지정가능한 장점으로 다양한 곳에서 많이 사용될 것이다.
    */

    const example = { key1: 'value', key2: 'value2' }
    // console.log(example) // ***
    // console.log(example.key1) // ***
    // console.log(example.key2) // ***












    // 오브젝트의 복사

    /*
        아래의 obj2는 obj1의 복사본이 아니다.
        즉, 다른 변수처럼 개체를 복사하는 것처럼 작동하지 않는다. 
        즉,
        다른 변수의 경우에,
            const a = 1, const b = 2, a = b, console.log(a) 의 순서로 코딩하면,
            결과값이 2가 나오지만,
        아래 오브젝트의 경우에는,        
            첫번째 콘솔로그는 3
            두번째 콘솔로그는 1이 나올 것 같지만 그렇지 않고 3이 나온다.
     */

    const obj1 = { a: 1, b: 2 }
    const obj2 = obj1
    obj1.a = 3
    // console.log(obj1.a) // ***
    // console.log(obj2.a) // ***

    /*
        이러한 결과값이 나오는 이유는 다음과 같다.
        오브젝트는 "주소"를 참조한다.
        즉, 선언이나 변경을 할 때는 "값"이 아닌 "그 주소"를 대입시키는 거라서,    
        결국 같은 주소를 참조하게 되는 것이다.
        같은 것을 바라보는 두개의 변수가 되는 것이다.
        주소를 복사해서 새로운 주소로 만들어야만
        우리가 생각하는 "새 변수로의" 대입이 될 것이다. 
        그 방법은 아래와 같이 JSON 클래스의 두 명령어를 사용한다.
            1. JSON.stringify : 문자화를 해서 카피한다.
            2. JSON.parse : 파싱(컴퓨터가 이해할 수 있는 형태로 바꾼다.)해서 페이스트한다.
    */

    const obj3 = JSON.parse(JSON.stringify(obj1))
    obj1.b = 4
    // console.log(obj1.b) // 4 // ***
    // console.log(obj3.b) // 2 // ***

    // 캐스팅(Casting) : 데이터타입의 변경
    const cast1 = '1'
    // Number(cast1) // 숫자 타입으로 변경
    // if (cast1 === 1) { // ***
    //     console.log('cast는 숫자 1입니다.') // ***
    // } // ***
    const cast2 = 1
    // String(cast2) // 문자열 타입으로 변경
    // if (cast2 === '1') { // ***
    //     console.log('cast2는 문자열 "1"입니다.') // ***
    // } // ***













   // 어레이

    /*
        어레이는 (어레이)리스트, 배열, 일람이라고도 불린다.
        어레이는 '숫자, 문자열, 불린, 객체' 등 여러개의 변수를 하나에 담는다.
        또한 어레이는 let으로 지정시 유동적이며, 데이터의 추가나 삭제가 가능하다.
    */

    // 초기화
    let array1 = []

    // 추가 업데이트
    array1.push(1)
    array1.push(2)
    array1.push(3)
    array1.push(4)
    array1.push(5)

    // 삭제 업데이트
    array1.pop()
    array1.pop()
    // console.log(array1) // ***
    // console.log(array1[0]) // ***
    // console.log(array1[1]) // ***

    let array2 = [1, 3, 3, 4, 4, 6]
    array2.push(7, 9)
    // console.log(array2[0]) // ***
    // console.log(array2[1]) // ***    
    // 제일 마지막것을 꺼내는 법
    // console.log(array2[array2.length - 1]) ***

    // 지정한 수만큼의 인덱스를 가진 배열 생성 (파이썬에서의 range(n)과 동일)
    let array3 = [...Array(5).keys()] // = [0, 1, 2, 3, 4]
    // console.log(array3) // ***
    // 0부터 20까지의 밸류가 들어간 배열 자동생성 (=python의 range(20)과 동일함)
    let array33 = [...Array(21).keys()]



    // 다양한 종류의 배열 예시
    let rainbow = ['빨', '주', '노', '초', '파', '남', '보']
    let weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    // console.log(rainbow[2]) // ***
    // console.log(weekdays[2]) // ***









    // 어레이와 오브젝트의 차이 ~ JSON 데이터구조

    /* 
        결정적인 차이는 다음과 같다.
        1. 어레이는 인덱스라고 불리우는 순서가 있다. [0], [1] ...        
            꺼낼 때, 키로 꺼내지 않고, 인덱스(들어가있는 순서)로 꺼낸다.
        2. 어레이는 아이템이 아니라 "상자"다.
            그러므로 오브젝트를 비롯해 스트링, 넘버 등 다양한 아이템을 담을 수 있다. 
            그러나, 반대로 오브젝트에 키의 밸류값으로 배열을 넣는 것도 가능하다.
        3. 어레이 변수는 For문 등의 반복문을 돌릴 때 필요하다.
            여러개의 값을 배열에 넣고 반복을 통해 한번에 처리할 때 필요하게 된다.
            오브젝트는 값을 꺼낼 때 키를 "찾아서" 검색하는 느낌에 가깝다.

        예를 들면, 고객정보를 담게 된다면,
        array는 [{고객1}, {고객2}, {고객3}, ...]와 같이 해당 고객 하나하나를 의미하게 될 거고,
        object는 { id: dev123, pw: 1234, realName: azuma, ... } 등의 정보가 들어갈 것이다.
        어레이안에 오브젝트를 넣게 된다면 완성된 형태는
        let users = [{ id: dev123, pw: 1234, ... }, { id: runner, pw: 132315, ... }, ...]
        형태가 될 것이며,
        users[0]부터 users[n]까지를 호출하면 해당 오브젝트 전체를 호출하게 될 것이고,
        users[0].id를 호출하면 해당 유저의 id만을 호출하게 되는 것이다.
        
        이러한 형태를 JSON 데이터구조라고 한다.
            팀 프로젝트 현장에서는 주로 JSON 형태의 데이터구조를 사용한다.
            JSON은 Array<Object> = [{}, {}, {}, ...]의 형태를 가진다.
            JSON 데이터구조의 예시는 아래와 같다.
    */

    let obj = { a: 1, b: 2 }    
    // alert(obj.a)
    // alert(obj.b)
    const o1 = { id: 'user1', pw: '1234' }
    const o2 = { id: 'user2', pw: '2345' }
    const o3 = { id: 'user3', pw: '3456' }
    // console.log(o1.id) // key: value
    // console.log(o2.id) // key: value
    // console.log(o3.pw) // key: value
    const a1 = []
    a1.push(o1)
    a1.push(o2)
    a1.push(o3)
    // console.log(a1) // [{}, {}, {}] = JSON 형태
    
    










    // 세트

    /*
        코딩을 하다보면, 경우에 따라
        어레이 중에서 중복값을 제거해야하는 경우가 있다.
        이때 세트를 사용한다.

        세트는 어레이로부터 정보를 받아서, 중복된 것을 삭제한다. 
        이를 두고 현장에 따라 "유니크" 처리라고도 부른다.

        세트는 아래와 같이 선언한다.
        const 세트명 = new Set(어레이명);

        세트는 아래와 같이 다시 어레이로 변경해서 사용한다.
        const 새로운어레이명 = Array.from(세트명)

        
     */

    // 어레이로부터 세트 선언: 어레이의 중복제거를 위해 쓴다.
    const array4 = [1, 2, 3, 4, 4, 5]
    const mySet = new Set(array4)
    // console.log(mySet) // ***

    // 추가 업데이트: 추가에서도 중복값은 여전히 들어가지지 않는다.
    // mySet.add(4) // ***
    // mySet.add(5) // *** 
    // mySet.add(6) // ***
    // console.log(mySet) // ***

    // 삭제 업데이트
    // mySet.remove(1) // ***
    // mySet.remove(2) // ***

    // 세트를 다시 어레이화
    const array5 = Array.from(mySet)
    // console.log(array5) // ***












    // 콘솔로그의 정체

    /*
        콘솔로그는 사실, 오브젝트다.
        그 안에 있는 key중 log라는 키를 사용하는 것이다.
        이렇게 객체 안에서 담아서 키를 처리하는 방식은 다른 언어에서도 사용된다.
        클래스.메소드(파라미터) 식으로 처리하는 백엔드 언어들을 여럿 볼 것이다.
        파이썬, 자바... 등등. (순수한 PHP의 경우에는 이것을 사용하지 않더라..)
        그래서 이러한 언어들을 "객체지향"언어라고 부르는 것이다.
    */
    // console.log(console) // ***
    // console.error("ERROR!") // *** console 클래스 안에 명령어중 error














    // 캐스팅 ***
    // let age = prompt("몇살인가요?") // *** prompt는 매우 오래된 JS. 지금은 인풋에 담지만 빨리 처리하기 위해 우선 써본다.
    if (age >= 30 || age < 40) {
        console.log("당신은 30대시군요.")
    }
    


}
