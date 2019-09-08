# https://leetcode.com/contest/weekly-contest-153/problems/make-array-strictly-increasing/
import os, sys, re, math
from math import inf, ceil, floor
from operator import itemgetter
from functools import wraps, cmp_to_key, reduce, lru_cache
from itertools import count, combinations, permutations
from collections import namedtuple, defaultdict, Counter, deque
from queue import Queue
from bisect import bisect_left, bisect_right
from copy import deepcopy

sys.setrecursionlimit(1000000)



class Solution:
  def makeArrayIncreasing(self, arr1, arr2):  # -> int
    arr2 = sorted(set(arr2))

    @lru_cache(None)
    def cached_bisect(n):
      return bisect_left(arr2, n)

    @lru_cache(None)
    def dp(i, n):
      opCnt = 1 if n != arr1[i] else 0

      if i == 0:
        return opCnt

      choices = []

      bsi = cached_bisect(n)
      if bsi != 0:
        choices.append(opCnt + dp(i-1, arr2[bsi-1]))

      if arr1[i-1] < n:
        choices.append(opCnt + dp(i-1, arr1[i-1]))

      # print('i, n, choices:', i, n, choices)

      return min(choices or [inf])

    for n in arr1:
      cached_bisect(n)
    for n in arr2:
      cached_bisect(n)


    choices = [dp(len(arr1)-1, n) for n in arr2 if n != arr1[-1]]
    choices.append(dp(len(arr1)-1, arr1[-1]))
    ans = min(choices)

    return ans if ans != inf else -1

if __name__ == '__main__' and ('SJDEAK' in os.environ):
  from utils.tree import TreeNode, array2TreeNode
  from utils.linkedlist import ListNode, integerListToListNode
  from icpc_util import dump_args


  def test(*args):
    print('输入数据: ', *args)
    print('结果: ', Solution().makeArrayIncreasing(*args), end='\n-----\n')


  test([1,5,3,6,7], [1,3,2,4])
  test([1,5,3,6,7], [4,3,1])
  test([1,5,3,6,7], [1,6,3,3])
  test([53140479,75802402,47912265,59793700,23588003,99564022,7474829,48017688,20405895,57074698,11167249,43289932,49190059,47012446,34215637,71559360,22489359,85839858,89358809,71637108,90606515,28028870,60533533,57677160,56898455,76128986,46593697,87910556,95998651,32922158,62961253,79427600,47005727,12444866,55871081,25293252,71881411,17864086,27281325,5812920,3205287,44447402,25225009,58386668,96783819,44719102,38517749,75130208,96806447,6564242,84809721,81705748,13933267,85659750,62603581,18080520,73857207,11153530,17035713,4854844,74642907,81425358,45608069,75279792,61190975,78006882,81085577,35368548,88077795,62974262,54260941,77456984,97120967,3147082,49214545,68506508,49554411,76104606,72872981,63669504,42262863,87396402,33182745,54188980,82385651,26516998,88121181,41690792,28583383,23655706,54955745,57209564,95006203,38469998,32520357,48372816,11195231,57456130,32961961,55074052,44317187,29212374,5489389,11972344,59515623,65352170,18068849,68536364,46502155,53226558,25608757,55139488,46375279,20666322,17038649,28383060,67295763,3556262,29168253,56591176,77984759,8123066,35897601,71704188,94117403,74590990,15583685,87917808,75502207,2971042,8361929,72107172,33515811,13447542,83211533,98575512,12361735,95752074,95173009,98137804,95641131,50310366,6048853,75334208,39552911,66453874,279641,74773236,78702387,50013510,14192541,16531176,71398167,74040922,76849953,84828188,37259835,49999022,52851429,81372816,3701151,97432386,46689513,92800068,72414275,31820566,55135789,22521656,84222247,92562730,45566641,76044396,27564875,136574,76908405,17229024,24283311,79644434,89984121,99596948,14008915,93704678,7112893,15109768,68248887,18536954,51982401,34337468,21642587,20548174,37729541,94227504,83268799,65206498,15171593,47416804,56179811,96361142,8849485,37231576,10576199,60132298,52519121,71312908,18850155,87314206,78839445,32893568,50110159,12254130,87237785,1415732,12818803,90208646,81722845,96055336,81065303,27267994,47964001,49516124,19380091,32549870,31311653,37760208,69758175,74308994,85589801,33031044,38384771,42350422,53983853,58567800,39625063,11119978,86359025,36126892,95859083,26487742,18833333,64039968,13621999,48543314,44047033,54117588,14056339,32810790,35722493,21571528,10834807,9107002,61007745,56629756,52523163,52865422,29536069,73472112,51545343,54954274,97221705,35371812,57396131,40751606,28534413,97929496,21555847,90818570,18636049,22426188,62200491,94685278,51049173,57867968,40407055,60405746,90785497,11215732,16217779,72843462,16653853,49030248,85025943,2754266,31946145,14193820,43151803,32360750,50253925,58040848,33523231,4210882,56327017,68394180,74933699,3184790,39210413,2037688,72780711,81626282,45097521,3919340,78880459,82839038,1435893,56482912,69288495,67207826,73134841,94952468,23970771,45640038,61453885,9623304,99169719,25423226,19014849,16647228,53300955,27163598,86716037,14136752,14025023,40167778,11473545,91728740,43568099,29129526,22989,82469976,83420359,55990858,45956177,88889228,75540971,16470174,34143765,49278976,69930319,56812338,44788505,52310196,18864371,43156486,123997,30255016,19584471,26843930,14951393,41316060,40284155,20577134,61965733,61831760,64817759,13632258,12927913,72401668,48766211,45579990,57764589,38700024,35123687,4665322,37788529,16186412,65823243,41744446,98356021,75921056,57757551,34560466,2875705,70681684,98356755,44763302,54428797,44398920,84578039,84108986,22188801,45219708,81367579,32112910,41153733,81706736,7565439,95149730,99786185,934308,50076963,58972790,26101261,11421080,94799879,20023434,24995217,4010444,84094507,5725150,741973,13998400,84711055,75317618,6277721,29555444,41854771,99903558,87635357,36871400,20472599,85567578,20206369,53299484,39657531,26804398,35952357,34534544,29655455,236098,54253801,52731204,29761859,9827094,54656045,89807160,33945895,4570922,51379633,50967660,52395851,98945662,94336629,50426336,68769711,59144978,99704441,8261780,39566419,35046374,10628541,98719880,1586487,41507322,7112001,96598716,28662619,99407694,32337157,40799280,97128639,85425634,11870729,29283556,41128547,32139190,47989581,17987032,53607751,78088394,80555217,97387532,78913899,31121950,16994197,22951552,99691983,77055666,27898521,84716596,51706739,63046022,7292125,95624744,88538967,98848410,12646241,48825948,87257979,86353134,11859749,74648784,66780895,91570818,58119209,39838340,49205635,60271446,90980205,88923256,63234407,28611434,19598065,46462380,31288971,78677182,71518901,81852704,61261551,79568466,62489273,21626068,13366675,44831782,5306109,82608072,72830583,73683770,26543233,73756924,36939163,99386766,54778693,43368048,36087039,32101666,9074249,36669988,96977571,54930422,44053901,73033496,58216839,29147402,62139153,4243788,61940907,48081502,43029461,84937152,59986959,83024626,58557401,51407732,2756019,43732166,73629981,53015656,25309847,20578010,47206817,46944156,61455803,60798510,52755813,82498576,89655071,94589634,28750953,51499460,10408131,94150294,54150061,55338168,50548647,89527978,86774833,1296364,56162507,70078718,34873589,33958752,32083759,28552594,56069113,53761812,93175507,50730342,47829053,71004424,25589175,6331770,11273665,5446972,12292315,32455118,22391685,64778160,74441279,97375074,54000521,79583332,80175331,96549942,62228941,70690136,97243591,88807498,69562449,94591884,40054763,59722910,68972309,27975424,35514447,16683570,35194137,5865140,15859443,94649350,86011485,28880296,97593047,56414234,81117153,15589596,24433915,53169518,91637925,64226640,58647135,16287746,47049897,14723588,9296387,36873686,21537261,9131768,84590055,11820522,75543409,92833580,10234635,78920510,47828277,16373920,57163375,13037522,97630009,71055188,62207251,27366310,5418877,82872136,26535671,17280442,75102209,57419132,84482587,71785998,14278341,40795376,21745279,21462690,93607625,31675812,61667875,44046454,70017549,91964824,34941703,32698250,48995985,30673868,22438955,85996510,47696469,15619392,36526223,33898866,43711833,95746548,49890099,7421766,59024541,41012200,23336727,96122458,82138657,72430620,97646651,65887918,97074149,72569488,1231263,55360578,12434665,49375300,21873987,43761686,36874285,23928376,76130855,54944298,22544817,47177068,321611,29238142,1293429,21522656,11393199,77615378,20201849,12224660,43706195,90943462,63153597,6286472,59130935,67344122,81083201,29691580,16528731,88512334,22427141,27443504,17440959,78736610,38839561,27847652,86888803,22538678,58073421,59804888,82736967,87831498,94576081,8201228,41189483,91825438,89866901,37848960,36285647,3473586,28562329,89675828,22410867,79771526,71012317,54345768,45516887,93053082,98320225,36297820,42855035,38758126,20241189,55734224,22997983,76386946,87366697,17168004,13598083,27567958,44634989,22249592,76798567,66792810,10697457,52297900,95910027,81929150,46990773,4660512,61544943,53757778,40189369,3615956,19213203,89613094,42475005,53878472,57848183,46540858,56693633,66913020,8151963,60694670,28934725,43791472,51070463,52727842,21727049,32635684,26417315,25830902,55110541,76918808,8545415,75270410,53975569,59822924,66646699,19913310,65867733,11584448,56644111,53636338,30969305,36743796,28410035,55374534,90257181,12022376,59560343,99662042,28817057,34257820,24533691,80039214,65835877,90666256,12815903,68390338,2147177,23216580,81763779,81510806,1004973,40693944,10916775,47647658,59045681,17331692,78750411,50716158,34856181,52051040,97748783,98370706,65304057,74368020,55336659,73838694,99759165,98010376,78430647,69198202,7261633,69967932,20183259,66085838,17265029,17674160,54463551,37943394,83306633,59908964,93879523,14713398,72993229,66227544,96627399,99931978,4260177,49640332,39907819,85476254,72566037,70595584,72165199,21602098,90646297,9873332,34538483,61078790,33174365,99909288,73162455,79581722,20018401,39470812,4006651,25366382,12866725,84114000,11658079,11951618,57206185,99929604,65474307,95504598,65918701,43146744,94606823,23195626,77692273,52328236,53742603,98514238,11541557,48490656,39160175,74433234,96515897,13827924,5990163,25859238,39861117,67516232,20322295,55849402,22321153,67052924,65465627,38342414,47694533,39048688,19869567,94278562,28069065,51672996,6852387,49110390,52419597,37031576,7085831,92799626,80438929,53766348,19539243,33332702,7558997,63273280,91079055,61737842,88458073,48380404,849971,75605318,22223517,89806824,33401623,73960282,77407777,95184924,77363771,96812718,92713701,38833040,36343455,67643970,2111721,58480196,73859907,90672406,59686189,21334072,80781607,80672298,55846577,2682476,8238923,83105662,3218549,40086240,90274223,49964562,57273721,74119316,50724691,7566822,82177725,29264520,49867575,56491514,88561985,62395324,34103387,84753230,7890181,34556464,25975231,83607010,47994121,60139748,56295011,61661622,15382861,41403096,44643399,66281418,76640721,53797644,53444203,84004382,6320533,11919232,18424527,71082674,28626073,75589172,28537203,28278406,23430877,86209064,54201687,78833306,81144417,59850332,38119803,47150574,86135333,85489104,72931807,13081218,25985065,1379204,84277123,71782742,81084525,39871096]
,[87666791,92853610,73924081,76859820,1140363,95003326,4036021,14410272,15281135,81329234,63456697,29053652,1029011,98882854,31292925,52945608,76093047,17435962,49264257,52615164,76953243,56636558,43231813,36220016,4140543,45519138,59484489,42815012,44281251,17263094,45115277,3733016,46234503,28146954,58269457,63734348,61403307,99866718,1464277,30383552,23989007,32979442,60147417,398964,73579699,63855302,86006045,91832680,81578135,65437658,12358817,11552924,21892027,78172718,72148325,79552272,4901663,86574530,60187241,17646276,1891779,72399254,67903149,38413752,85153191,67385258,711473,13729516,38307019,5530110,451829,39746400,37527855,44455570,69839609,66167828,75382483,59827558,87215421,94426376,25132983,10650490,59559105,74125884,84604379,92113358,8430469,32307888,38879551,76879970,67757449,40881252,90647011,11377206,97749197,61821272,56306375,40899402,25539153,48988812,78815979,57845662,33418005,23100672,32489039,82791730,66632985,80611252,55984883,46465030,42892893,80522664,85078999,7833114,372193,97042396,78385915,6047086,79541157,4482128,36073823,90225666,15877545,3810564,33743363,62365398,13971437,69701112,13184999,72292330,30276465,91862572,27159563,99768126,98015029,78532512,71635823,58340050,94448953,58750036,43745299,28523430,96981117,79505480,15403767,48876218,70386945,58905468,16347163,67632398,76243141,37624048,3729535,60675490,4540873,5987236,61308451,1929846,15524109,85286808,10866695,55446410,12549521,83554764,73865259,71200734,83811925,45200448,84722575,3480946,16632409,73483764,7072307,2469958,77585309,90215656,61980439,28104538,37405217,80123932,40050235,70166958,61277413,77962384,80427679,94466370,35671785,29702724,95982915,41537046,11572013,40873272,70815015,39486506,74996145,86951532,26836555,4803454,21559413,32699616,98457775,29324050,1816697,97171348,21217107,38619366,57093309,96706696,19745591,37191418,87961153,51115708,28463195,65869134,23198213,10827568,29069247,63594466,37062921,99914468,55120995,39106230,77546829,17287384,35428679,98908618,7527633,16064012,96235627,54492958,48790421,83001216,55947215,5309362,21388697,30266676,15087219,16000134,42752221,60826152,2491479,30527898,2174561,81706076,82399099,60420334,54635813,57260496,62203615,84786562,8706089,42561924,80677251,20573782,92527981,29834360,43113831,4130922,66849265,91794092,12905355,19109054,57334453,77337888,44615407,38878546,20387769,23850964,89911955,94497062,75006717,59890632,71412087,62084666,53694081,68335100,53802395,32630670,54253125,31085936,76908799,35729186,1199689,67904292,51159459,66809846,21677197,79204632,37150599,52447242,3933201,21990732,61420715,85779038,92360917,36511680,78265359,18497010,83904729,344436,42782131,74440134,85710621,26618472,10129559,85264858,27441057,54772380,28793019,4564526,88083045,314384,10524191,18781890,97145193,44988868,74750659,91648662,15814317,3305144,21133479,12868778,42605873,21567212,46870475,50957566,77429749,75476832,31576623,91297682,1209081,67741972,69520851,23418982,78075197,18717448,98176439,47655802,41101249,623420,3616987,79512782,3451781,29895088,35781183,91685730,82891145,84578660,8648931,19355958,33390029,76682840,93786823,5967178,14445137,33783692,74558699,10422430,14142741,84885504,22081871,93838642,3417625,52030132,17409011,89703942,96895837,29254056,22403543,1780506,93064417,7622620,54520059,26886254,47434405,42365264,93877343,22177794,73149097,33250820,83577859,72733910,53344493,34455800,41372135,89380586,5800049,82577196,90530315,45585726,69794869,4289952,44512623,41502930,14793273,92060756,8008211,45513382,52048253,7761736,5178103,6128314,3139073,14614140,88842267,27162382,7591877,83351792,27327359,70230690,41429961,70120612,33512227,3733366,61306637,35175320,56003847,47214218,58892945,95581644,14985515,47580382,59544149,61679680,14019983,4436082,64387417,58482676,22120499,90043718,15898525,34372072,52670743,64634458,86646049,44772124,68506171,7163822,36177381,95030672,95847583,23149378,41041897,42971204,16126787,49959446,57455149,40329528,3058215,97877802,67240113,6743148,63027787,73329534,25712245,59973856,26049967,93821714,4786553,29509780,82308691,54050790,75899069,53636488,41070647,38412538,68441921,5560764,81502043,76496206,59364869,11003440,49790399,68918242,10235145,35491044,33784419,55917238,4954701,43543256,81663815,26898634,89339345,26690572,96361323,79430174,94644885,75636352,68582095,12363442,9768601,11153460,81621107,82107014,22135261,96255784,95770711,31099546,92261729,46456668,40165243,87368174,16392229,30170576,60285151,75231362,64749865,77208196,5802115,99167830,54722157,57416824,38824551,52257386,21269489,17329836,78111883,8159934,25178293,63426592,52175599,84340562,74280633,77976532,44798099,97783334,28051453,28393416,94215799,43092026,27515521,33928444,63720603,19298446,29961029,26717296,57028351,86497058,14523209,37778468,14700707,39345654,51603085,12807704,26230663,7071754,42324497,24492620,40713643,48521054,57243093,72650432,46029839,57747954,34688729,58940788,30326451,80522182,71427101,80147560,25320087,51756762,22660769,67633052,46600123,90791982,39023717,14700304,24452383,41432514,10925161,70972612,54492867,47419030,42613165,92744376,42899111,23026602,66550321,59376108,76025035,43301118,40861685,27541344,83908399,77853074,68622329,48111636,36009683,16477030,18702909,74990344,27363255,10625658,71096001,48716604,30243291,54494926,50449029,71124912,10346815,9697378,95680649,1924452,32590307,52989494,57438413,35617368,5367495,3782986,40737873,83363724,41096171,88539294,99326229,53589504,87649103,93927474,50594585,85166772,44953843,49366790,60328797,31989160,27805143,25022234,29896417,13095388,24818427,22096750,99646117,65720912,37148511,59244034,73630377,50620164,57405699,52450774,64214765,90475512,10745831,88356586,92910449,1075244,42309131,8449854,46318133,63016096,30358127,33327058,70717241,71441492,78316307,38561702,64051581,91726920,95027447,30533050,48436481,88879740,70310427,85270030,49524165,92720880,61020543,8386466,3387593,54248868,32261667,10110582,14257421,17276312,27759367,57364874,80552337,81322956,76743723,73716446,77648981,31542848,38924431,47220594,86594905,23672820,21616691,75019846,536221,40238824,84786967,49288794,92610849,5853724,58950203,11017134,40561125,85686928,10956959,66174018,16537321,82324804,75134019,20691478,40073261,62887736,68161063,82740010,55111345,55538796,40030539,61398910,13458037,75893728,23803055,3999762,94318201,85955476,78067539,27701222,64142013,12940936,25879863,76270330,95644993,96220860,16423771,9132110,82158853,66431280,84235711,1813730,47830281,40586980,23268195,33500598,94408013,52976600,40351047,633290,93697745,72972,91678827,99498782,47834261,59735424,18222287,98849458,51939225,94375732,39189619,93115526,21471197,54004776,17167191,86171802,41060449,50035292,17736059,56126958,66559525,5657808,18285791,50721666,81945897,89705348,83839619,53917014,15817837,9154936,79431783,44971114,23888881,27834284,64286347,40804030,20618933,31783200,35389423,61698130,65173945,91837652,19713427,27365158,26258429,74816456,83763319,50339642,32440449,99935996,31074459,25801614,77354309,14197104,34407679,19777314,8724809,96099620,97518755,73519862,13203085,18962200,603271,60884234,15874833,74794828,40806827,63722590,16730325,25769152,6418959,79636722,81721561,24491892,44376499,85981382,66218013,9164392,19398551,86456282,54361249,69782428,74806715,76630318,97136229,17990160,34537247,77818562,81523305,85104068,53427651,66201494,88035757,44678840,48233639,97286314,80348721,18991084,47442123,21124862,68324597,99235936,44169519,57301138,58959353,6368532,87005651,78702950,17217597,49404168,57874103,99563642,80568257,80063292,6886107,53390542,32509317,9954224,20968767,8764002,43197833,75241060,18085091,97262390,13041613,45251416,77800647,35369546,57020497,60409740,59679211,6137502,34561045,2686976,2987087,82034482,43356441,75927988,20717555,10119174,39651165,38210216,52947927,27907610,45232097,61663964,77314555,45151598,15471781,10531664,40610911,60084482,96432297,58332932,53986819,7061462,40363501,66931192,41615335,93056234,32566641,85431084,41700619,6771262,92894005,97520032,80479855,3823314,40054585,21584468,96757779,48716198,97991549,52274504,89284599,85602234,60918017,15239292,34672667,4452366,90206661,82679280,38908287,29115298,10883785,49102244,74068771,390518,53685261,78384536,90413063,39876490,24862353,61546956,50460459,58369246,45345877,69675328,21442703,25330802,34101593,80718324,22775859,57441862,19152797,42196968,42881559,9525082,45662241,15369244,6939707,69331374,25468389,85039760,85542559,79284802,80111593,27229764,51877187,29325846,26726445,20707640,14490919,67401258,55564209,21191020,51508043,47225726,29757813,53664736,92632751,30293010,25454201,6389652,63685971,89254374,41165501,66163592,39128119,46763770,35254337,95894972,46053467,14320974,93160453,17036336,88831935,62082786,89473033,86215652,10326627,39673526,39629901,80186840,46455111,53524170,59117265,86225420,42228075,22007582,8899221,66195584,24442575,23815858,77779609,3057204,11618419,31462022,55570653,59790376,97172055,25279642,77592161,75874140,44055419,35358446,83587365,36797392,29084895,84112770,60772393,29512580,55581059,7026262,45192557,72185464,82139751,25587562,60215025,86930092,97757067,54813630,66937525,92067872,59872751,28577106,34442937,7000276,8516755,89950502,24817661,88566472,69362039,47689530,32449921,53518332,77523355,94954894,37139525,86930800,90217983,36569122,20123721,92850724,14831779,35823606,65902477,87583000,90727559,67003402,66833,77506124,72916907,48547934,95732437,4445632,2622479,67632370,43371225,55343476,12988595,54230726,82416669,4774248,66475927,21174746,95913377,47656348,43986619,83778862,53032549,32924688,38327327,3772354,15236969,86395332,22407363,78096534,36838829,4978104,92014759,6109610,41959985,42172140,60172235,71803390,52046581,78108000,93553455,43275666,55336953,41023764,48352467,76810854,24963389,76826376,58584247,75184762,70356161,55927356,41567195,23274702,24627845,37490864,9967935,93051746,48953993,26352228,79486947,32578102,49479117,81986904,43038663,30668106,99356497,33414796,82226155,2615966,94289173,96924416,23587151,59074610,73163289,13490612,36818931,39414022,72458589,28069800,9205463,28066842,80858337,58789596,56615675,28178286,1802405,87412048,60694879,16154370,56407465,81780740,79147267,70783958,94420205,39976952,6102247,60333802,55627121,11209772,58199819,99113022,43560501,17416864,90226543,63094738,30083641,66341460,75047187,88386470,78513277,62417992,54423799,11863738,39905281,26781820,77837595,1537294,12332229,6142704,70356607,53161378,20596681,84255396,19701027,30432630,53775885,53146520,86065159,21790346,70630289,43270860,36679211,89805278,1232469,21466688,76195727,16010610,11351385,56385524,86498867,55491654,4928925,59638248,48454935,66482778,74103841,68924700,10938683,46922158,46347237,39768720,26370207,21583170,46731241,90027332,98960195,68091926,78399277,13810488,33632295,40385066,26494129,3447148,33357131,97632638,76733045,44339424,61445295,75322386,688249,69805716,63117651,93326054,55456957,63333256,92582455,48415994,97667905,60330940,19693147,10820430,96622597,67110960,41326015,62704354,88083209,8267236,42424675,69472438,75358029,74195160,27107143,91714506,13968849,430348,68553067,47126814,83922325,92606336,44155087,45035442,32865689,81767220,75493235,58521478,51898845,21409320,7242071,13920666,61780065,27485532,83740795,8258030,55920421,94571984,18464223,67944322,62797609,45814404,60883075,28416086,61383021,77554808,70607207,91926890,60458481,45313708,72310155,19663550,18336181,56012832,11576047,92108114,91555513,39766484,14307987,30946086,67581949,77769160,38239863,49591866,55097217,92159228,37614491,39801486,26897221,25683312,69142527,21825058,39679049,84794660,2731683,38966262,74782093,66354968,80895111,47895306,32795921,45699660,19262635,27108190,97887701,82688704,79289103,65425394,75405529,54597236,29434035,83365574,6300957,97795432,92055447,47440858,58552225,58486172,95047099,4188718,49964901,98206224,71580959,23978690,21482345,72532676,94085571,85504918,58368429,66511032,92964775,55602090,47467825,70062572,64239307,64914174,58963701,42160992,28576303,78982034,40525817,32349716,55379667,36667750,6631229,33250312,87500727,60835450,8733633,94393660,11364827,41676494,60353413,96862640,34860095,1286242,4987529,74091108,40591843,71600694,22666701,67510104,51895239,5434186,61235537,28132748,81002219,246430,17242901,78743552,29549391,16521778,57881881,89900980,12334579,4010246,53130845,86122920,79979991,59051290,31055585,28589276,95325691,13264238,72435109,31130192,30084447,95677442,76205481,55706628,31314179,15302102,65793261,38940152,62377703,66183146,60648049,91981100,96089611,1984062,29161781,60018336,71118447,77744594,84466745,54762324,59989011,21871014,74881405,72435784,1166071,44542138,67828481,68220028,70775067,93801742,2931909,68040688,20729983,41410210,9755593,99410340,45523747,54795126,26337037,42355096,75940615,51013258,51189905,48970188,71869739,99250654,49350741,39592256,51979151,61386866,99754841,95547124,15476019,77412934,46467741,58180328,24615447,82814810,56175137,62726428,36807483,31444654,68961765,94495632,19111583,42990914,152553,51755332,36807491,94751510,54708269,70243384,22110759,99007530,10193073,32964460,67763531,42174590,81108597,92393952,33587119,47145490,51772025,20770196,46312275,52862182,79991997,23038088,905271,92128506,98123585,85602236,2244443,81715278,47381509,87918384,75465919,2053858,77370889,83014884,62410339,85786550,24708173,17731032,25171527,56375242,86828241,20656908,74532459,41863710,3184021,60838016,1368271,88171954,65205657,36203828,63600755,17764742,30100701,48781352,5455191,577946,77987681,18676316,53159035,3851246,9435429,62437840,52621023,74632578,39487785,10996100,41311107,95481942,86875245,31083384,6848359,64248426,94610161,91723180,99080075,14159294,24056245,40823584,55759855,82293842,32540089,56399828,24982419,68484390,92780285,83395784,50986871,37148218,93021057,2760444,16196507,37480334,55746117,88324464,73074431,53142818,1843529,82064932,25738147,10525942,47941005,59217944,57749639,86782474,12013073,28334156,52022699,48681566,47015125,47885248,74519311,90851314,91854553,41405044,69945011,98448326,14108701,85389160,47441815,67198682,13633441,87455388,57026235,83888686,18172773,38120976,86881823,56553922,46391657,41454276,89630915,10747542,10608813,76674744,40796327,72475306,49125169,92970732,80537547,90679806,62858741,17941600,84820015,38752146,47595513,56234260,40811987,35259238,89480253,78145288,42975415,31627130,25968833,32974396,31257051,55957966,75583621,69072048,44657727,9226338,91627913,27804516,86418915,22783542,65208525,89165400,57069511,95795274,68959057,85002124,35049707,32915870,42038549,54344960,65773903,28812082,73188121,12531892,68624115,12594438,94889053,820648,76107223,82016282,36846305,28382940,15357691,2847598,37672101,92460368,64161119,5437698,62281897,51643140,73509635,13316822,17251821,68721400,74675431,84140266,83549553,71189548,12998667,79543870,96610613,55347872,63529327,67480274,13246521,61336148,94951699,642214,70122365,37170504,56844279,56659386,22001153,99317884,77995547,31036430,6613957,74141936,70297215,695970,40850633,18536868,6369059,51419254,38159373,69831320,15227399,64472202,36184721,46695628,58743595,38362078,65335125,79538496,48807823,48903794,9183321,10318068,20230195,5502278,57687453,46195176,32479767,11768154,67188769,17760796,4423995,36313774,94555877,72728720,10374303,9219138,45064937,96343364,81970243,88494358,22119981,16489016,81134631,54359082,40602289,95132780,76249931,56796286,43289205,64980704,21604271,3151378,15924089,27979924,27215699,70568934,86678205,63777416,80239159,69594106,14345025,33253564,61427291,32890702,28158981,34556464,18026687,53940962,86559497,29649380,67852387,91162294,39672909,15554520,51278919,20972746,71069905,28577292,45167467,19087902,31003797,69787008,33326543,81523122,91757977,85285940,93034867,31464070,65693405,37960744,67941975,64991898,10873953,50634332,83388539,42891758,63685925,87257296,5336031,5826178,60484905,99802500,43861123,55953494,15133037,65507704,51599975,40398698,12212721,47503788,7810443,99563454,26372021,875552,93831663,24091474,48371641,8517844,51656851,63689254,31866365,43322312,47256695,61388346,6878593,41644028,15722651,80385166,77950533,51456880,18953215,75033378,96474185,31336484,47224483,2322422,86097549,50613272,63685767,29853706,57164817,95308364,60389547,25018974,48406741,96145856,28822799,25526258,51620313,68394868,88951731,65412294,24462365,68831592,74410135,7132122,78686881,53521820,14467003,16344878,15034469,78976016,62670623,64682178,33951081,86817732,64141763,36649622,99743917,13959352,88550055,85773994,65850673,96575468,72098507,17495550,823797,66922336,96743471,23830674,57203449,20579604,23173075,66516326,43900733,65258504,47868087,23922042,44025025,30329404,7473883,46262222,270981,44456112,58517055,45472354,53455241,89366372,44724451,80001078,6894029,12951896,43739591,89573706,30374737,83754892,10678763,46780062,5300501,98495488,70461775,25942834,97474841,72222900,67527155,61502470,99607389,85281448,43314391,27891738,10318049,73699804,71065083,62915950,41830565,91469648,83828319,4112130,89928617,32378884,59248643,38335958,29710573,34369016,71322599,98073578,11976049,95828524,27452171,71495742,56958517,14967200,51713647,57742034,50966841,56535124,35245843,44421542,4198525,40435016,80853751,3384506,83330817,61019260,36951323,84902414,50884805,46381552,61447039,50701474,87605705,3867300,23070243,25242486,11960845,40896920,46829319,91240586,77148561,33339340,76010795,14573534,17332821,66114112,18202255,47782258,52520025,18013428,5341491,73064518,36365213,58892520,11868439,14374746,37639201,4881436,63881531,70467758,33511909,5205392,92077215,77694274,91842793,29146180,52923715,94314262,45752621,69153080,6596391,22915882,61536433,64940140,54542667,71642750,10759797,66786016,36588975,26393106,68818297,2986388,71816019,5997542,90346941,41971848])
else:
  print = lambda *args, **kwargs: None
  dump_args = lambda func: func
