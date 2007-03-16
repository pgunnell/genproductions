#ifndef DTRawToDigi_DTControlData_h
#define DTRawToDigi_DTControlData_h

/** \class DTROS25Data
 *  The collection containing DT ROS25 status data.
 *
 *  $Date: 2006/06/25 15:31:38 $
 *  $Revision: 1.3 $
 *  \author M. Zanetti - INFN Padova
 */

#include <EventFilter/DTRawToDigi/interface/DTDDUWords.h>
#include <DataFormats/FEDRawData/interface/FEDHeader.h>
#include <DataFormats/FEDRawData/interface/FEDTrailer.h>

#include <vector>


using namespace std;

typedef std::pair<int, DTROBHeaderWord> DTROBHeader;   // IJ
typedef pair<int, DTTDCMeasurementWord> DTTDCData;
typedef pair<int, DTTDCErrorWord> DTTDCError;
typedef pair<DTLocalTriggerDataWord, int> DTSectorCollectorData;

class DTROS25Data {

public:

 /// Constructors
 DTROS25Data(int ROSId = 0): theROSId(ROSId) {}


 /// Destructor
 virtual ~DTROS25Data() {}

 /// Setters  ///////////////////////
 inline void setROSId(const int & ID) { theROSId = ID; }

 inline void addROSTrailer( const DTROSTrailerWord & word)  { theROSTrailer = DTROSTrailerWord(word) ; }
 inline void addROSError( const DTROSErrorWord & word)  { theROSErrors.push_back(word); }
 inline void addROSDebug( const DTROSDebugWord & word)  { theROSDebugs.push_back(word); }
 inline void addROBHeader( const DTROBHeader & robHeader)  { theROBHeaders.push_back(robHeader); }   // IJ
 inline void addROBTrailer( const DTROBTrailerWord & word)  { theROBTrailers.push_back(word); }
 inline void addTDCMeasurement( const DTTDCMeasurementWord & word)  { theTDCMeasurements.push_back(word); }
 inline void addTDCData( const DTTDCData & tdcData)  { theTDCData.push_back(tdcData); }
 inline void addTDCError( const DTTDCError & tdcError)  { theTDCError.push_back(tdcError); }
 inline void addSCData ( const DTSectorCollectorData & scData) { theSCData.push_back(scData); }

 /// Getters ////////////////////////
 inline int getROSID() const { return theROSId; }

 inline const DTROSTrailerWord & getROSTrailer() const {return theROSTrailer;}
 inline const vector<DTROSErrorWord>& getROSErrors() const {return theROSErrors;}
 inline const vector<DTROSDebugWord>& getROSDebugs() const {return theROSDebugs;}
 inline const std::vector<DTROBHeader>& getROBHeaders() const {return theROBHeaders;}    // IJ
 inline const vector<DTROBTrailerWord>& getROBTrailers() const {return theROBTrailers;}
 inline const vector<DTTDCMeasurementWord>& getTDCMeasurements() const {return theTDCMeasurements;}
 inline const vector<DTTDCData>& getTDCData() const {return theTDCData;}
 inline const vector<DTTDCError>& getTDCError() const {return theTDCError;}
 inline const vector<DTSectorCollectorData>& getSCData() const {return theSCData;}

 /// Cleaners  ////  IJ  /////////////

 inline void cleanROSTrailer()  { theROSTrailer = 0; }
 inline void cleanROSError()  { theROSErrors.clear(); }
 inline void cleanROSDebug()  { theROSDebugs.clear(); }
 inline void cleanROBHeader() { theROBHeaders.clear(); }
 inline void cleanROBTrailer() { theROBTrailers.clear(); }
 inline void cleanTDCMeasurement()  { theTDCMeasurements.clear(); }
 inline void cleanTDCData() { theTDCData.clear(); }
 inline void cleanTDCError() { theTDCError.clear(); }
 inline void cleanSCData() { theSCData.clear(); }


private:

 int theROSId;

 DTROSTrailerWord theROSTrailer;
 vector<DTROSErrorWord> theROSErrors;
 vector<DTROSDebugWord> theROSDebugs;
 vector<DTROBHeader> theROBHeaders;     // IJ
 vector<DTROBTrailerWord> theROBTrailers;
 vector<DTTDCMeasurementWord> theTDCMeasurements;
 vector<DTTDCData> theTDCData;
 vector<DTTDCError> theTDCError;
 vector<DTSectorCollectorData> theSCData;

};


class DTDDUData {

public:

 /// Constructor
 DTDDUData(const FEDHeader & dduHeader, const FEDTrailer & dduTrailer):
   theDDUHeader(dduHeader),
   theDDUTrailer(dduTrailer)
 {}


 /// Destructor
 virtual ~DTDDUData() {}

 /// Setters
 inline void addDDUHeader( const FEDHeader & word)  { theDDUHeader = word; }
 inline void addDDUTrailer( const FEDTrailer & word)  { theDDUTrailer = word; }
 inline void addROSStatusWord( const DTDDUFirstStatusWord & word) {
   theROSStatusWords.push_back(word);
 }
 inline void addDDUStatusWord( const DTDDUSecondStatusWord & word) {
   theDDUStatusWord = word;
 }

 /// Getters
 inline const FEDHeader & getDDUHeader() const {return theDDUHeader;}
 inline const FEDTrailer & getDDUTrailer() const {return theDDUTrailer;}
 inline const vector<DTDDUFirstStatusWord> & getFirstStatusWord() const {
   return theROSStatusWords;}
 inline const DTDDUSecondStatusWord & getSecondStatusWord() const {
   return theDDUStatusWord;}


private:

 FEDHeader theDDUHeader;
 FEDTrailer theDDUTrailer;
 vector<DTDDUFirstStatusWord> theROSStatusWords;
 DTDDUSecondStatusWord theDDUStatusWord;

};


#endif
