// Code generated by protoc-gen-go.
// source: test.proto
// DO NOT EDIT!

/*
Package example is a generated protocol buffer package.

It is generated from these files:
	test.proto

It has these top-level messages:
	Test
*/
package example

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"
import google_protobuf "github.com/golang/protobuf/ptypes/timestamp"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Corpus int32

const (
	Corpus_UNIVERSAL Corpus = 0
	Corpus_WEB       Corpus = 1
	Corpus_IMAGES    Corpus = 2
	Corpus_LOCAL     Corpus = 3
	Corpus_NEWS      Corpus = 4
	Corpus_PRODUCTS  Corpus = 5
	Corpus_VIDEO     Corpus = 6
)

var Corpus_name = map[int32]string{
	0: "UNIVERSAL",
	1: "WEB",
	2: "IMAGES",
	3: "LOCAL",
	4: "NEWS",
	5: "PRODUCTS",
	6: "VIDEO",
}
var Corpus_value = map[string]int32{
	"UNIVERSAL": 0,
	"WEB":       1,
	"IMAGES":    2,
	"LOCAL":     3,
	"NEWS":      4,
	"PRODUCTS":  5,
	"VIDEO":     6,
}

func (x Corpus) String() string {
	return proto.EnumName(Corpus_name, int32(x))
}
func (Corpus) EnumDescriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

type Test struct {
	Label string                     `protobuf:"bytes,1,opt,name=label" json:"label,omitempty"`
	Type  int32                      `protobuf:"varint,2,opt,name=type" json:"type,omitempty"`
	Reps  int64                      `protobuf:"varint,3,opt,name=reps" json:"reps,omitempty"`
	Hello Corpus                     `protobuf:"varint,4,opt,name=hello,enum=example.Corpus" json:"hello,omitempty"`
	Time  *google_protobuf.Timestamp `protobuf:"bytes,5,opt,name=time" json:"time,omitempty"`
}

func (m *Test) Reset()                    { *m = Test{} }
func (m *Test) String() string            { return proto.CompactTextString(m) }
func (*Test) ProtoMessage()               {}
func (*Test) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *Test) GetTime() *google_protobuf.Timestamp {
	if m != nil {
		return m.Time
	}
	return nil
}

func init() {
	proto.RegisterType((*Test)(nil), "example.Test")
	proto.RegisterEnum("example.Corpus", Corpus_name, Corpus_value)
}

func init() { proto.RegisterFile("test.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 268 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x09, 0x6e, 0x88, 0x02, 0xff, 0x34, 0x8e, 0xdd, 0x4a, 0xf3, 0x40,
	0x10, 0x86, 0xbf, 0x6d, 0x76, 0xd3, 0x76, 0x3e, 0x7f, 0x96, 0xc1, 0x83, 0xd0, 0x13, 0x83, 0x20,
	0x04, 0x0f, 0xb6, 0x50, 0xaf, 0xa0, 0xa6, 0x41, 0x02, 0xb1, 0x91, 0x4d, 0xda, 0x82, 0x67, 0x09,
	0xac, 0x55, 0xd8, 0xb0, 0x4b, 0xb2, 0x05, 0xbd, 0x16, 0x6f, 0x56, 0x92, 0xd8, 0xb3, 0x77, 0xde,
	0x79, 0x98, 0x79, 0x00, 0x9c, 0xea, 0x9c, 0xb0, 0xad, 0x71, 0x06, 0xa7, 0xea, 0xab, 0x6a, 0xac,
	0x56, 0x8b, 0xdb, 0xa3, 0x31, 0x47, 0xad, 0x96, 0x43, 0x5d, 0x9f, 0xde, 0x97, 0xee, 0xb3, 0x51,
	0x9d, 0xab, 0x1a, 0x3b, 0x92, 0x77, 0x3f, 0x04, 0x68, 0xa9, 0x3a, 0x87, 0x37, 0xc0, 0x74, 0x55,
	0x2b, 0x1d, 0x90, 0x90, 0x44, 0x73, 0x39, 0x0e, 0x88, 0x40, 0xdd, 0xb7, 0x55, 0xc1, 0x24, 0x24,
	0x11, 0x93, 0x43, 0xee, 0xbb, 0x56, 0xd9, 0x2e, 0xf0, 0x42, 0x12, 0x79, 0x72, 0xc8, 0x78, 0x0f,
	0xec, 0x43, 0x69, 0x6d, 0x02, 0x1a, 0x92, 0xe8, 0x6a, 0x75, 0x2d, 0xfe, 0x04, 0x44, 0x6c, 0x5a,
	0x7b, 0xea, 0xe4, 0xb8, 0x45, 0x01, 0xb4, 0x17, 0x08, 0x58, 0x48, 0xa2, 0xff, 0xab, 0x85, 0x18,
	0xed, 0xc4, 0xd9, 0x4e, 0x94, 0x67, 0x3b, 0x39, 0x70, 0x0f, 0x6f, 0xe0, 0x8f, 0x07, 0xf0, 0x12,
	0xe6, 0xbb, 0x6d, 0xba, 0x4f, 0x64, 0xb1, 0xce, 0xf8, 0x3f, 0x9c, 0x82, 0x77, 0x48, 0x9e, 0x38,
	0x41, 0x00, 0x3f, 0x7d, 0x59, 0x3f, 0x27, 0x05, 0x9f, 0xe0, 0x1c, 0x58, 0x96, 0xc7, 0xeb, 0x8c,
	0x7b, 0x38, 0x03, 0xba, 0x4d, 0x0e, 0x05, 0xa7, 0x78, 0x01, 0xb3, 0x57, 0x99, 0x6f, 0x76, 0x71,
	0x59, 0x70, 0xd6, 0x23, 0xfb, 0x74, 0x93, 0xe4, 0xdc, 0xaf, 0xfd, 0xe1, 0xeb, 0xe3, 0x6f, 0x00,
	0x00, 0x00, 0xff, 0xff, 0xb4, 0x76, 0x28, 0xb7, 0x38, 0x01, 0x00, 0x00,
}
